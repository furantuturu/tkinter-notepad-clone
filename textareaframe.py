from tkinter import *

class TextFrame:
    def __init__(self, window) -> None:
        self.window = window
        self.textarea = Text(master=self.window, undo=True, height=self.window.winfo_screenheight(), font=('Arial', 16))
        self.scrollbar_y = Scrollbar(master=self.window, orient=VERTICAL, command=self.textarea.yview)
        self.scrollbar_x = Scrollbar(master=self.window, orient=HORIZONTAL, command=self.textarea.xview)
        self.status_bar_frame = Frame(master=self.window, height=24)

        self.textarea.grid(row=0, column=0, sticky=EW)
        self.scrollbar_y.grid(row=0, column=1, sticky=NS)

        self.textarea.config(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        Label(master=self.status_bar_frame, width=24).grid(row=2, column=0)
        Label(master=self.status_bar_frame, text="Ln 1, Col 1", relief=GROOVE, justify=LEFT, anchor=W).grid(row=2, column=1, ipadx=40)
        Label(master=self.status_bar_frame, text="100%", justify=LEFT, anchor=W).grid(row=2, column=2, ipadx=5)
        Label(master=self.status_bar_frame, text="Windows (CRLF)", relief=GROOVE, justify=LEFT, anchor=W).grid(row=2, column=3, ipadx=10)
        Label(master=self.status_bar_frame, text="UTF-8", justify=LEFT, anchor=W).grid(row=2, column=4, ipadx=30)