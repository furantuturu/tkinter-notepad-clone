from tkinter import *
from tkinter import font
import menus
import textareaframe

window = Tk()
window_w = 727
window_h = 500
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

x = int((screen_w / 2) - (window_w / 2))
y = int((screen_h / 2) - (window_h / 2))

window.title("Untitled")
window.geometry(f"{window_w}x{window_h}+{x}+{y}")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

font = font.Font(family='Arial', size=16)

if __name__ == "__main__":
    textframe = textareaframe.TextFrame(window=window, default_font=font)
    menutab = menus.Menus(window=window, textarea=textframe.textarea, font=font ,status_bar_frame=textframe.status_bar_frame, scrollbar_x=textframe.scrollbar_x)
    window.mainloop()
