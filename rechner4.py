from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import simpledialog, messagebox
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from farbe4 import *


def calculate_expression(exp):
    information = {}
    edge_options = Options()
    # edge_options.add_argument("--headless")
    service = Service(executable_path=r"C:\edgedriver_win64 (1)\msedgedriver.exe")
    information.update({"options": edge_options, "service": service})
    driver_Edge = webdriver.Edge(service=information["service"], options=information["options"])

    try:
        driver_Edge.get("https://iask.ai")

        search_box = WebDriverWait(driver_Edge, 18).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
        input_f = f"Zusammenfassendes Ergebnis für diesen mathematischen Ausdruck: {exp}"
        search_box.send_keys(input_f)
        search_box.send_keys(Keys.RETURN)
        print("Die Suche wurde erfüllt")

        result_span = WebDriverWait(driver_Edge, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[jsname='VssY5c']"))
        )
        print("Das Ergebnis wurde gefunden.")

    except Exception as e:
        result = f"Fehler beim Rechnen : {e}"
        print(result)
    finally:
        driver_Edge.quit()


def create_rechner4(frame):
    numeric_buttons = []

    def in_calculate():
        exp = entry.get()
        result = calculate_expression(exp)
        result_label.config(text=result)

    entry = tk.Entry(frame, width=60, font=("Arial", 20), bd=100, relief="flat", background="#e0e0e0", justify="right")
    entry.pack(pady=20, padx=20)

    def pck(e):
        if e == calculate_button:
            return e.pack(pady=20, padx=10, fill=tk.X)
        if e == result_label:
            e.pack(pady=20, padx=20, fill=tk.X)

    calculate_button = ttk.Button(frame, text="rechnen", command=in_calculate)
    pck(calculate_button)

    result_label = tk.Label(frame, text="", wraplength=800, font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333")
    pck(result_label)

    numeric_buttons.append(calculate_button)
    create_color_option_menu4(frame, numeric_buttons)

    def in_settings():
        settings_window = tk.Toplevel(frame)
        settings_window.title("Settings")

        tk.Label(settings_window, text="Btns Label ändern:").pack(pady=10)

        for btn in numeric_buttons:
            btn_text = btn.cget("text")
            tk.Button(settings_window, text=btn_text, command=lambda b=btn: change_btn_text(b)).pack(pady=5)

        tk.Label(settings_window, text="Buttons Ändern:").pack(pady=10)

        for btn in numeric_buttons:
            btn_text = btn.cget("text")
            tk.Button(settings_window, text=f"Position ändern '{btn_text}'", command=lambda b=btn: move_button(b)).pack(
                pady=5)

    def change_btn_text(button):
        text1 = button.cget("text")
        text2 = simpledialog.askstring("Button Text wechseln:", f"Gib neuer text für button ein '{text1}':")
        if text2:
            if text2 in [btn.cget("text") for btn in numeric_buttons]:
                messagebox.showerror("Fehler", "Button text hat ein Problem")
                return
            else:
                button.config(text=text2)

    def get_pack_options(button):
        pack_info = button.pack_info()
        return pack_info.get('side', 'top'), pack_info.get('a', 'center'), pack_info.get('padx', 0), pack_info.get(
            'pady', 0)

    def get_neue_pack_options(button, side1, a1, padx1, pady1):
        side2 = simpledialog.askstring("Button Position ändern",
                                       f"Gib neue 'side' für button '{button.cget('text')}' (richtige: {side1}):",
                                       initialvalue=side1)
        a2 = simpledialog.askstring("Button Position ändern",
                                    f"Gib neue 'a' für button '{button.cget('text')}' (richtige: {a1}):",
                                    initialvalue=a1)
        padx2 = simpledialog.askinteger("Button Position ändern",
                                        f"Gib neue 'padx' für button '{button.cget('text')}' (richtige: {padx1}):",
                                        initialvalue=padx1)
        pady2 = simpledialog.askinteger("Button Position ändern",
                                        f"Gib neue 'pady' für button '{button.cget('text')}' (richtige: {pady1}):",
                                        initialvalue=pady1)
        return side2, a2, padx2, pady2

    def move_button(button):
        side1, a1, padx1, pady1 = get_pack_options(button)
        side2, a2, padx2, pady2 = get_neue_pack_options(button, side1, a1, padx1, pady1)

        if side2 is not None and a2 is not None:
            button.pack_forget()
            button.pack(side=side2, anchor=a2, padx=padx2, pady=pady2)

    settings_button = ttk.Button(frame, text='Settings', command=in_settings)
    settings_button.pack(side=tk.BOTTOM, anchor=tk.E, pady=2, padx=2)
    numeric_buttons.append(settings_button)
