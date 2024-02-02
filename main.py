from tkinter import *
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

scrollbar_y = Scrollbar(master=window, orient=VERTICAL, command=textarea.yview)
scrollbar_x = Scrollbar(master=window, orient=HORIZONTAL, command=textarea.xview)

scrollbar_y.grid(row=0, column=1, sticky=NS)

textarea.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

status_bar_frame = Frame(master=window, height=24)
Label(master=status_bar_frame, width=24).grid(row=2, column=0)
Label(master=status_bar_frame, text="Ln 1, Col 1", relief=GROOVE, justify=LEFT, anchor=W).grid(row=2, column=1, ipadx=40)
Label(master=status_bar_frame, text="100%", justify=LEFT, anchor=W).grid(row=2, column=2, ipadx=5)
Label(master=status_bar_frame, text="Windows (CRLF)", relief=GROOVE, justify=LEFT, anchor=W).grid(row=2, column=3, ipadx=10)
Label(master=status_bar_frame, text="UTF-8", justify=LEFT, anchor=W).grid(row=2, column=4, ipadx=30)

menutab = menus.Menus(window=window, textarea=textarea, status_bar_frame=status_bar_frame, scrollbar_x=scrollbar_x)

if __name__ == "__main__":
    window.mainloop()
