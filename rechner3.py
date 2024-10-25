from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import simpledialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from farbe3 import *


# (def) Zum Senden der Forderungen an den relevanten Service
def calculate_expression(mtm_opt):
    dicttDv = {}
    service = Service(executable_path=r"C:\edgedriver_win64 (1)\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    dicttDv.update({"service": service, "driver": driver})

    try:
        dicttDv["driver"].get("https://www.google.com/search")
        search_box = WebDriverWait(dicttDv["driver"], 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(mtm_opt)
        search_box.send_keys(Keys.RETURN)
        print("Suche wurde erfüllt")

        # Wartezeiten zum Anzeigen der des Ergbinisses
        rslt_span = WebDriverWait(dicttDv["driver"], 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[jsname='VssY5c']"))
        )
        print("Ergbeniselement wurde gefunden")

        # Extrahieren das Ergebnis aus dem 'tag' <span> mit der ID jsname='VssY5c'
        rslt = rslt_span.text
        print("Ergebnis wurde gefunden:{}".format(rslt))
    except Exception as e:
        rslt = e
        print("Fehler beim Ergebnisempfang:{}".format(rslt))
    else:
        print("Mathematische Operationen wurden durchgeführt")
    finally:
        dicttDv["driver"].quit()

    return rslt


# (def) zum Empfang der Informationen von dem Nutzer und Anzeigen der Ergebinsse
def create_rechner3(frame):
    numeric_buttons = []

    def in_calculate():
        try:
            num1 = float(txt1.get())
            operator = operator_var.get()
            num2 = float(txt2.get())
            mtm_opt = f"{num1} {operator} {num2}"
            rslt = calculate_expression(mtm_opt)
            rslt_label.config(text=rslt)
            print(f"Letztes Ergebnis: {rslt}")
        except Exception as e:
            rslt_label.config(text=f"Error: {e}")

    def clear_entry():
        txt1.delete(0, tk.END)
        txt2.delete(0, tk.END)
        operator_entry.delete(0, tk.END)

    def create_label_and_entry(label_text, **kwargs):
        tk.Label(frame, text=label_text).pack()
        entry = tk.Entry(frame, **kwargs)
        entry.pack()
        return entry

    def create_buttons():
        buttons = [
            ('rechnen', in_calculate),
            ('auslöschen', clear_entry)
        ]
        for text, command in buttons:
            btn = tk.Button(frame, text=text, command=command)
            btn.pack()
            numeric_buttons.append(btn)

    create_color_option_menu3(frame, numeric_buttons)

    txt1 = create_label_and_entry("Erste Nummer")
    operator_var = tk.StringVar()
    operator_entry = create_label_and_entry("Mathematische Operatoren wie: (...,+,-,*,/,//,**,%,sin, cos, tan, log)",
                                            textvariable=operator_var)
    txt2 = create_label_and_entry("Zweite Nummer")

    rslt_label = tk.Label(frame, text="")
    rslt_label.pack()

    create_buttons()

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
                                    f"Gib neue 'anchor' für button '{button.cget('text')}' (richtige: {a1}):",
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

    settings_button = tk.Button(frame, text='Settings', command=in_settings)
    settings_button.pack(side=tk.BOTTOM, anchor=tk.E, pady=2, padx=2)
    numeric_buttons.append(settings_button)
