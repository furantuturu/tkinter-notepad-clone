import time
from tkinter import *

class Menus:
    def __init__(self, window, textarea) -> None:
        self.window = window
        self.textarea = textarea
        self.menubar = Menu(master=window)

        self.window.config(menu=self.menubar)

        filemenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=quit)
        filemenu.add_command(label="New Window", command=quit)
        filemenu.add_command(label="Open...", command=quit)
        filemenu.add_command(label="Save", command=quit)
        filemenu.add_command(label="Save As...", command=quit)
        filemenu.add_separator()
        filemenu.add_command(label="Page Setup...", command=quit)
        filemenu.add_command(label="Print...", command=quit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)


        editmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="Copy", command=self.copy)
        editmenu.add_command(label="Paste", command=self.paste)
        editmenu.add_command(label="Delete", command=self.cut)
        editmenu.add_separator()
        editmenu.add_command(label="Find...", command=quit)
        editmenu.add_command(label="Find Next", command=quit)
        editmenu.add_command(label="Find Previous", command=quit)
        editmenu.add_command(label="Replace...", command=quit)
        editmenu.add_command(label="Go To...", command=quit)
        editmenu.add_separator()
        editmenu.add_command(label="Select/All", command=self.select_all)
        editmenu.add_command(label="Time/Date", command=self.time_date)


        formatmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Format", menu=formatmenu)
        formatmenu.add_command(label="Word Wrap", command=quit)
        formatmenu.add_command(label="Font...", command=quit)


        viewmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="Zoom", command=quit)
        viewmenu.add_command(label="Status Bar", command=quit)


        helpmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="View Help", command=quit)
        helpmenu.add_command(label="Send Feedback", command=quit)
        helpmenu.add_separator()
        helpmenu.add_command(label="About Notepad", command=quit)
        
        
    # Edit menu commands
    def undo(self):
        # self.textarea.event_generate("<<Undo>>")
        self.textarea.edit_undo()

    def cut(self):    
        self.textarea.event_generate("<<Cut>>")

    def copy(self):   
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def select_all(self):
        self.textarea.event_generate("<<SelectAll>>")
    
    def time_date(self):
        current_time = time.strftime("%I:%M %p %d/%b/%Y")
        self.textarea.insert(END, current_time)