import os
from tkinter import *
from tkinter import filedialog, messagebox
import menus

window = Tk()
window_w = 727
window_h = 500
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

x = int((screen_w / 2) - (window_w / 2))
y = int((screen_h / 2) - (window_h / 2))

window.geometry(f"{window_w}x{window_h}+{x}+{y}")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

textarea = Text(master=window, undo=True, height=window_h, font=('Arial', 16))
textarea.grid(row=0, column=0, sticky=EW)
scrollbar = Scrollbar(master=window, orient=VERTICAL, command=textarea.yview)
scrollbar.grid(row=0, column=1, sticky=NS)
textarea.config(yscrollcommand=scrollbar.set)

menutab = menus.Menus(window=window, textarea=textarea)

if __name__ == "__main__":
    window.mainloop()
