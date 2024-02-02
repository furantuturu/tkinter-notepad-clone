import os
import time
import webbrowser
import AppOpener
from tkinter import *
from tkinter import filedialog, messagebox

class Menus:
    def __init__(self, window, textarea, status_bar_frame, scrollbar_x) -> None:
        self.window = window
        self.textarea = textarea
        self.status_bar_frame = status_bar_frame
        self.scrollbar_x = scrollbar_x
        self.status_bar_toggle = True
        self.word_wrap_toggle = True
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
        editmenu.add_command(label="Find...", command=self.find)
        editmenu.add_command(label="Find Next", command=quit)
        editmenu.add_command(label="Find Previous", command=quit)
        editmenu.add_command(label="Replace...", command=quit)
        editmenu.add_command(label="Go To...", command=quit)
        editmenu.add_separator()
        editmenu.add_command(label="Select/All", command=self.select_all)
        editmenu.add_command(label="Time/Date", command=self.time_date)


        formatmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Format", menu=formatmenu)
        formatmenu.add_command(label="Toggle Word Wrap", command=self.word_wrap)
        formatmenu.add_command(label="Font...", command=self.font)


        viewmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="Zoom", command=self.zoom)
        viewmenu.add_command(label="Toggle Status Bar", command=self.status_bar)


        helpmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="View Help", command=self.view_help)
        helpmenu.add_command(label="Send Feedback", command=self.send_feedback)
        helpmenu.add_separator()
        helpmenu.add_command(label="About Notepad", command=self.about)
                
        self.word_wrap()
        self.status_bar()
        
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

    def find(self):
        find_menu_window = Tk()
        find_menu_window.title("Find")
        find_menu_window.resizable(False, False)

        Label(master=find_menu_window, text="Find what:").grid(row=0, column=0, pady=10)
        Entry(master=find_menu_window, width=32).grid(row=0, column=1, columnspan=3)
        
        Button(master=find_menu_window, text="Find Next", width=9).grid(row=0, column=4, padx=5)
        Button(master=find_menu_window, text="Cancel", width=9).grid(row=1, column=4)
        
        Label(master=find_menu_window, text="Direction").grid(row=1, column=2)

        radio_btn_var = IntVar()
        Radiobutton(master=find_menu_window, text="Up", variable=radio_btn_var, value=1).grid(row=2, column=2)        
        Radiobutton(master=find_menu_window, text="Down", variable=radio_btn_var, value=2).grid(row=2, column=3)
        
        matchcase_var = IntVar()
        wraparnd_var = IntVar()
        Checkbutton(master=find_menu_window, text="Match case", variable=matchcase_var, onvalue=1, offvalue=2).grid(row=2, column=0)   
        Checkbutton(master=find_menu_window, text="Wrap around", variable=wraparnd_var, onvalue=1, offvalue=2).grid(row=3, column=0)   
    
    def select_all(self):
        self.textarea.event_generate("<<SelectAll>>")
    
    def time_date(self):
        current_time = time.strftime("%I:%M %p %d/%b/%Y")
        self.textarea.insert(END, current_time)
    
    # Format menu commands
    def word_wrap(self):
        if self.word_wrap_toggle:
            self.textarea.config(wrap=WORD)
            self.scrollbar_x.grid_remove()
            self.word_wrap_toggle = False

        else:
            self.textarea.config(wrap=NONE)
            self.scrollbar_x.grid(row=1, column=0, sticky=EW)
            self.word_wrap_toggle = True
    
    def font(self):
        pass
    
    # View menu commands
    def zoom(self):
        pass

    def status_bar(self):
        if self.status_bar_toggle:
            self.status_bar_frame.grid(row=2, column=0, sticky=E)
            self.status_bar_toggle = False

        else:
            self.status_bar_frame.grid_remove()
            self.status_bar_toggle = True
            
    # Help menu commands
    def view_help(self):
        webbrowser.open_new_tab("https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA")
    
    def send_feedback(self):
        AppOpener.open("feedback hub")
    
    def about(self):
        messagebox.showinfo(title="About tk Notepad", message="This is an attempt to atleast clone notepad just for fun and test my coding skills in python and playing around in tkinter")