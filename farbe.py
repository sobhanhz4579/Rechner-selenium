import tkinter as tk
from tkinter import StringVar, OptionMenu, ttk


def chnge_color(event, selected_option, txtDisplay, numeric_buttons):
    selected_color = selected_option.get()
    txtDisplay.config(fg=selected_color, bg="white")

    for btn in numeric_buttons:
        btn.config(fg=selected_color, bg="White")


def create_color_option_menu1(cal, txtDisplay, numeric_buttons):
    def optt(x):
        if x == selected_option:
            return x.set(color[0])  # Default option
        if x == option_menu:
            x.grid(row=16, column=6, columnspan=5, pady=2, padx=2)
            x.bind("<Button-1>", lambda event: chnge_color(event, selected_option, txtDisplay, numeric_buttons))
            return x

    color = ["Red", "Orange", "Green", "Purple"]
    selected_option = StringVar(cal)
    optt(selected_option)

    option_menu = OptionMenu(cal, selected_option, *color)
    optt(option_menu)
