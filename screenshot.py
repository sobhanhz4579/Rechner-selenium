from tkinter import messagebox, IntVar, Checkbutton
from PIL import ImageGrab
from functools import wraps


def dec_screenshot(func):
    @wraps(func)
    def inner(screenshot_checkbox_var, *args, **kwargs):
        try:
            if not screenshot_checkbox_var:
                messagebox.showwarning("Warnung", " checkbox`s Screenshot  ist nicht gecheckt worden.")
                return
            result = func(screenshot_checkbox_var, *args, **kwargs)
            messagebox.showinfo("Screenshot", "Screenshot wurde gespeichert als 'calculator_screenshot.jpg'")
        except Exception as e:
            messagebox.showerror("Fehler", f"Screenshot ließ sich nicht machen: {e}")
        return result

    return inner


@dec_screenshot
def screenshot(screenshot_checkbox_var):
    # ImageGrab.grab().save(r"C:\Users\sobha\Desktop\Y_b\calculator_screenshot.jpg")
    ImageGrab.grab().save(r"C:\Users\sobha\Desktop\screen_cpt\calculator_screenshot.jpg")


def create_scr_checkbox(root):
    scr_checkbox_var = IntVar()
    screenshot_checkbox = Checkbutton(root, text="Screenshot machen", variable=scr_checkbox_var)
    if screenshot_checkbox:
        screenshot_checkbox.grid(row=10, column=0)
        return scr_checkbox_var
