from tkinter import *
from tkinter import simpledialog, messagebox
from farbe import *
import math


def create_rechner1(frame):
    text_input = tk.StringVar()
    listtNN1 = []

    frame.grid_rowconfigure(0, weight=1)
    a = 1
    while a <= 10:
        frame.grid_rowconfigure(a, weight=1)
        a += 1
    frame.grid_rowconfigure(10, weight=2)

    frame.grid_columnconfigure(0, weight=1)
    for i in range(1, 5):
        frame.grid_columnconfigure(i, weight=1)

    txDisplay = tk.Entry(frame, width=20, bd=0, font=('arial', 20, 'bold'), textvariable=text_input, insertwidth=30,
                         bg='powder blue', justify='right')
    txDisplay.grid(row=0, column=0, columnspan=5, pady=5, sticky="nsew")

    btn_style = {'font': ('Arial', 14), 'bd': 5, 'bg': '#f0f0f0', 'fg': '#000000', 'width': 5, 'height': 2}

    # in  Numeric buttons
    bttn = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
    ]
    numeric_buttons = []
    for (text, row, col) in bttn:
        button = tk.Button(frame, text=text,
                           command=lambda x=text: in_button_klick(x, txDisplay, listtNN1, result_label3_3), **btn_style)
        button.grid(row=row, column=col, sticky="nsew")
        numeric_buttons.append(button)

    # Operators buttons
    operators = ['+', '-', '*', '(', ')', '/', 'tan', 'sin', 'cos', 'C', 'log', 'sqrt']
    for i, operator in enumerate(operators):
        button = tk.Button(frame, text=operator, command=lambda x=operator: in_operator_klick(x, txDisplay),
                           **btn_style)
        button.grid(row=i // 3 + 1, column=3 + i % 3, sticky="nsew")
        numeric_buttons.append(button)
    create_color_option_menu1(frame, txDisplay, numeric_buttons)

    result_label3_3 = tk.Label(frame, font=('arial', 20, 'bold'), bd=10, justify='center')
    result_label3_3.grid(row=5, column=0, columnspan=5, pady=10)

    def in_settings():
        settings_window = tk.Toplevel(frame)
        settings_window.title("Settings")

        canvas = tk.Canvas(settings_window)
        scrollbar = tk.Scrollbar(settings_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        # canvas und scrollbar
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        tk.Label(scrollable_frame, text=" Buttons Label ändern:").pack(pady=10)

        for btn in numeric_buttons:
            btn_text = btn.cget("text")
            tk.Button(scrollable_frame, text=btn_text, command=lambda b=btn: change_button_text(b)).pack(pady=5)

        tk.Label(scrollable_frame, text="Postion von Buttons ändern :").pack(pady=10)

        for btn in numeric_buttons:
            btn_text = btn.cget("text")
            tk.Button(scrollable_frame, text=f"Position ändern: '{btn_text}'",
                      command=lambda b=btn: move_button(b)).pack(pady=5)

    def change_button_text(button):
        text1 = button.cget("text")
        text2 = simpledialog.askstring("Button Text wechseln:", f"Gib neuer text für button ein'{text1}':")
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
                                       f"Gib neue row für button ein '{button.cget('text')}' (richtige: {row1}):",
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
    settings_button.grid(row=15, column=6, columnspan=5, pady=2, padx=2)
    numeric_buttons.append(settings_button)


def in_button_klick(value, display, listtNN, result_label3_3):
    if value == '=':
        try:
            result = eval(display.get())
            listtNN.append(result)
            if result_label3_3:
                result_label3_3.config(text=f"Result: {[listtNN[i] for i in range(len(listtNN))]}")
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')
    else:
        display.insert(tk.END, value)


def in_operator_klick(opt, display):
    operations = {'sin': lambda nummer: math.sin(math.radians(nummer)),
                  'cos': lambda nummer: math.cos(math.radians(nummer)),
                  'tan': lambda nummer: math.tan(math.radians(nummer)), 'log': lambda nummer: math.log10(nummer),
                  'sqrt': lambda nummer: math.sqrt(nummer)
                  }
    try:
        if opt == 'C':
            display.delete(0, tk.END)
        elif opt in operations:
            exp = float(display.get())
            result = operations[opt](exp)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        else:
            display.insert(tk.END, opt)
    except Exception as ex:
        display.delete(0, END)
        display.insert(tk.END, "Error...")
