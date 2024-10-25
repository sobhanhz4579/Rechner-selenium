from tkinter import messagebox, Text, END, simpledialog
from farbe5 import *


def dec_save(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            messagebox.showinfo("Super,", "Note wurde erfolgreich gespeichert")
            return result
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler in : {str(e)}")

    return inner


def dec_load(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except FileNotFoundError:
            messagebox.showwarning("Warnung", "Keine vorherige Notiz gefunden")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler in : {str(e)}")

    return inner


@dec_save
def save_note():
    note = text.get("1.0", END)
    with open("note.txt", "w") as file:
        file.write(note)


@dec_load
def load_note():
    with open("note.txt", "r") as file:
        note = file.read()
        text.delete("1.0", END)
        text.insert("1.0", note)


def set_notes_frame(notebook):
    def pack_Form(m):
        if m == text:
            m.pack(padx=10, pady=10)
            return m
        if m == load_button:
            m.pack(side="top", padx=2, pady=2)
            return m
        if m == save_button:
            m.pack(side="top", padx=2, pady=2)
            return m

    notes_frame = ttk.Frame(notebook)
    notebook.add(notes_frame, text='Notes')
    numeric_buttons = []
    global text
    text = Text(notes_frame, wrap="word", height=20, width=50)
    pack_Form(text)

    load_button = ttk.Button(notes_frame, text="Load Note", command=load_note)
    pack_Form(load_button)

    save_button = ttk.Button(notes_frame, text="Save Note", command=save_note)
    pack_Form(save_button)
    numeric_buttons = [save_button, load_button]
    create_color_option_menu5(notes_frame, numeric_buttons)

    def in_settings():
        settings_window = tk.Toplevel(notes_frame)
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

    def get_pack_opts(button):
        pack_info = button.pack_info()
        return pack_info.get('side', 'top'), pack_info.get('a', 'center'), pack_info.get('padx', 0), pack_info.get(
            'pady', 0)

    def get_neue_pack_opts(button, side1, a1, padx1, pady1):
        side2 = simpledialog.askstring("Ändern Button Position",
                                       f"Gib neue 'side' für button '{button.cget('text')}' (richtige: {side1}):",
                                       initialvalue=side1)
        a2 = simpledialog.askstring("Ändern Button Position",
                                    f"Gib neue 'a' für button '{button.cget('text')}' (richtige: {a1}):",
                                    initialvalue=a1)
        padx2 = simpledialog.askinteger("Ändern Button Position",
                                        f"Gib neue 'padx' für button '{button.cget('text')}' (richtige: {padx1}):",
                                        initialvalue=padx1)
        pady2 = simpledialog.askinteger("Ändern Button Position",
                                        f"Gib neue 'pady' für button '{button.cget('text')}' (richtige: {pady1}):",
                                        initialvalue=pady1)
        return side2, a2, padx2, pady2

    def move_button(button):
        side1, a1, padx1, pady1 = get_pack_opts(button)
        side2, a2, padx2, pady2 = get_neue_pack_opts(button, side1, a1, padx1, pady1)

        if side2 is not None and a2 is not None:
            button.pack_forget()
            button.pack(side=side2, anchor=a2, padx=padx2, pady=pady2)

    settings_button = ttk.Button(notes_frame, text='Settings', command=in_settings)
    settings_button.pack(side=tk.BOTTOM, anchor=tk.E, pady=2, padx=2)
    numeric_buttons.append(settings_button)
