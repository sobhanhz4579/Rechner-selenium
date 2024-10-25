import tkinter as tk
from tkinter import StringVar, OptionMenu


def chnge_color(event, selected_option, numeric_buttons):
    selected_color = selected_option.get()

    for btn in numeric_buttons:
        btn.config(fg=selected_color, bg="White")


def create_color_option_menu3(cal, numeric_buttons):
    def optt3(x3):
        if x3 == selected_option:
            return x3.set(colors[0])  # Default option
        if x3 == option_menu:
            x3.pack(side=tk.BOTTOM, anchor=tk.E, pady=2, padx=2)
            x3.bind("<Button-1>", lambda event: chnge_color(event, selected_option, numeric_buttons))
            return x3

    colors = ["Red", "Orange", "Green", "Purple"]
    selected_option = StringVar(cal)
    optt3(selected_option)

    option_menu = OptionMenu(cal, selected_option, *colors)
    optt3(option_menu)
