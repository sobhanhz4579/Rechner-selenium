import tkinter as tk
from tkinter import StringVar, OptionMenu


def chnge_color(event, selected_option, txtDisplay, numeric_buttons):
    selected_color = selected_option.get()
    txtDisplay.config(fg=selected_color, bg="white")

    for btn in numeric_buttons:
        btn.config(fg=selected_color, bg="White")


def create_color_option_menu2(cal, txtDisplay, numeric_buttons):
    def optt2(x2):
        if x2 == selected_option:
            return x2.set(color[0])  # Default option
        if x2 == option_menu:
            x2.grid(row=16, column=14, columnspan=5, pady=2, padx=2)
            x2.bind("<Button-1>", lambda event: chnge_color(event, selected_option, txtDisplay, numeric_buttons))
            return x2

    color = ["Red", "Orange", "Green", "Purple"]
    selected_option = StringVar(cal)
    optt2(selected_option)

    option_menu = OptionMenu(cal, selected_option, *color)
    optt2(option_menu)
