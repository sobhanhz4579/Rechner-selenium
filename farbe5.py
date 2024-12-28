import tkinter as tk
from tkinter import StringVar, OptionMenu
from tkinter import ttk


def chnge_color(event, selected_option, numeric_buttons):
    selected_color = selected_option.get()

    style = ttk.Style()
    style.configure("Custom.TButton", foreground=selected_color, background="white")

    for btn in numeric_buttons:
        btn.config(style="Custom.TButton")


def create_color_option_menu5(cal, numeric_buttons):
    def optt5(x5):
        if x5 == selected_option:
            return x5.set(colors[0])
        if x5 == option_menu:
            x5.pack(side=tk.BOTTOM, anchor=tk.E, pady=2, padx=2)
            x5.bind("<Button-1>", lambda event: chnge_color(event, selected_option, numeric_buttons))
            return x5

    colors = ["Red", "Orange", "Green", "Purple"]
    selected_option = StringVar(cal)
    optt5(selected_option)

    option_menu = OptionMenu(cal, selected_option, *colors)
    optt5(option_menu)
