from tkinter import *
from tkinter import ttk
import tkinter as tk
from rechner1 import *
from rechner2 import *
from rechner3 import *
from rechner4 import *
from screenshot import *
from notes import *

cal = Tk()
cal.title("Calculator")
cal.geometry("900x900")
operator = ""
text_input = StringVar()

### ! notebook
notebook = ttk.Notebook(cal)
notebook.grid(row=0, column=0, columnspan=5, rowspan=10, sticky='NESW')
###
# rechner1_frame
rechner1_frame = ttk.Frame(notebook)
notebook.add(rechner1_frame, text="Rechner1")
create_rechner1(rechner1_frame)
###
# rechner2_frame
rechner2_frame = ttk.Frame(notebook)
notebook.add(rechner2_frame, text="Rechner2")
create_rechner2(rechner2_frame)
###
# rechner3_frame
rechner3_frame = ttk.Frame(notebook)
notebook.add(rechner3_frame, text="Rchner3 mit Google(selenium)")
create_rechner3(rechner3_frame)
###
# rechner4_frame
rechner4_frame = ttk.Frame(notebook)
notebook.add(rechner4_frame, text="Rechner4 mit AI(selenium)")
create_rechner4(rechner4_frame)
###
# notes_frame
notes_frame = set_notes_frame(notebook)


###
# screenshot
def check_screenshot(screenshot_checkbox_var):
    screenshot(screenshot_checkbox_var)


screenshot_checkbox_var = create_scr_checkbox(cal)
button = ttk.Button(cal, text="Check Screenshot", command=lambda: check_screenshot(screenshot_checkbox_var))
button.grid(row=11, column=0)

### cal
cal.mainloop()
