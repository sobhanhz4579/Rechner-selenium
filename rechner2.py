from tkinter import *
from tkinter import simpledialog, messagebox
from farbe2 import *


def create_rechner2(frame):
    listtNN2 = []

    def calculate():
        rechnen = input_entry.get()
        try:
            result = eval(rechnen)
            listtNN2.append(result)
            result_label2_2.config(text=f"Result: {[listtNN2[i] for i in range(0, len(listtNN2))]}")
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, 'Error')

    numeric_buttons = []

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
        text2 = simpledialog.askstring("Button Text wechseln:", f"Enter neuer text für button '{text1}':")
        if text2:
            if text2 in [btn.cget("text") for btn in numeric_buttons]:
                messagebox.showerror("Fehler", "Button text hat ein Problem")
                return
            else:
                button.config(text=text2)

    def get_position(button):
        grid_info = button.grid_info()
        return grid_info["row"], grid_info["column"]

    def get_neue_position(button, row1, column1):
        row2 = simpledialog.askinteger("Button Position ändern",
                                       f"Gib neue row für button ein'{button.cget('text')}' (richtige: {row1}):",
                                       initialvalue=row1)
        column2 = simpledialog.askinteger("Button Position ändern",
                                          f"Gib neue column für button ein '{button.cget('text')}' (richtige: {column1}):",
                                          initialvalue=column1)
        return row2, column2

    def move_button(button):
        row1, column1 = get_position(button)
        row2, column2 = get_neue_position(button, row1, column1)

        if row2 is not None and column2 is not None:
            button.grid(row=row2, column=column2)

    # settings button
    settings_button = tk.Button(frame, text='Settings', command=in_settings)
    settings_button.grid(row=15, column=14, columnspan=5, pady=2, padx=2)
    numeric_buttons.append(settings_button)

    input_entry = tk.Entry(frame, width=60, font=("Arial", 20), bd=100, relief="flat", background="#e0e0e0",
                           justify="center")
    input_entry.grid(row=1, column=2, columnspan=8, pady=20)

    btns2 = [
        (0, 4, 10, 2, 10, 10, 'auslöschen', 'center', 'w', lambda: input_entry.delete(0, END)),
        (0, 4, 2, 2, 10, 10, 'rechnen', 'center', 'e', calculate)
    ]

    for (row, column, columnspan, padx, pady, bd, text, justify, align, command) in btns2:
        butn2 = tk.Button(frame, padx=padx, pady=pady, bd=bd, text=text, justify=justify, font=('arial', 15, 'bold'),
                          command=command)
        butn2.grid(row=row + 2, column=column, columnspan=columnspan, sticky=align)
        numeric_buttons.append(butn2)
    result_label2_2 = tk.Label(frame, font=('arial', 20, 'bold'), bd=10, justify='center')
    result_label2_2.grid(row=3, column=0, columnspan=5, pady=10)

    create_color_option_menu2(frame, input_entry, numeric_buttons)
