import os
import time
import webbrowser
import AppOpener
from tkinter import *
from tkinter import filedialog, messagebox, font

class UI:
    def __init__(self, window) -> None:
        self.window = window
        self.status_bar_toggle = BooleanVar()
        self.word_wrap_toggle = BooleanVar()
        self.current_find_menu_window = None
        self.menubar = Menu(master=window)
        
        # ************************* TEXTAREA ***********************************************************
        self.font = font.Font(family="Arial", size=16)

        self.textarea = Text(master=self.window, undo=True, height=self.window.winfo_screenheight(), font=self.font)
        self.scrollbar_y = Scrollbar(master=self.window, orient=VERTICAL, command=self.textarea.yview)
        self.scrollbar_x = Scrollbar(master=self.window, orient=HORIZONTAL, command=self.textarea.xview)
        self.status_bar_frame = Frame(master=self.window, height=24)

        self.textarea.grid(row=0, column=0, sticky=EW)
        self.scrollbar_y.grid(row=0, column=1, sticky=NS)

        self.textarea.config(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)
        # *********************************************************************************************

        # ************************* MENUS ***********************************************************
        Label(master=self.status_bar_frame, width=24).grid(row=2, column=0)
        Label(master=self.status_bar_frame, text="Ln 1, Col 1", relief=GROOVE, justify=LEFT, anchor=W).grid(row=2, column=1, ipadx=40)
        Label(master=self.status_bar_frame, text="100%", justify=LEFT, anchor=W).grid(row=2, column=2, ipadx=5)
        Label(master=self.status_bar_frame, text="Windows (CRLF)", relief=GROOVE, justify=LEFT, anchor=W).grid(row=2, column=3, ipadx=10)
        Label(master=self.status_bar_frame, text="UTF-8", justify=LEFT, anchor=W).grid(row=2, column=4, ipadx=30)
        
        
        self.window.config(menu=self.menubar)

        filemenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="New Window", command=self.new_window)
        filemenu.add_command(label="Open...", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Save As...", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Page Setup...", command=self.page_setup)
        filemenu.add_command(label="Print...", command=self.print_content)
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
        formatmenu.add_checkbutton(label="Toggle Word Wrap", variable=self.word_wrap_toggle, command=self.word_wrap)
        formatmenu.add_command(label="Font...", command=self.change_font)


        viewmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=viewmenu)
        
        zoom_submenu = Menu(master=viewmenu, tearoff=0)
        viewmenu.add_cascade(label="Zoom", menu=zoom_submenu)
        zoom_submenu.add_command(label="Zoom In", command=self.zoom_in)
        zoom_submenu.add_command(label="Zoom Out", command=self.zoom_out)
        zoom_submenu.add_command(label="Restore Default Zoom", command=self.default_zoom)
        
        viewmenu.add_checkbutton(label="Toggle Status Bar", variable=self.status_bar_toggle, command=self.status_bar)


        helpmenu = Menu(master=self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="View Help", command=self.view_help)
        helpmenu.add_command(label="Send Feedback", command=self.send_feedback)
        helpmenu.add_separator()
        helpmenu.add_command(label="About Notepad", command=self.about)

        self.word_wrap_toggle.set(True)
        self.word_wrap()
        self.status_bar_toggle.set(True)
        self.status_bar()
        
    # File menu commands
    def new(self):
        self.window.title("Untitled")
        self.textarea.delete("1.0", END)
    
    def new_window(self):
        fresh_window = Tk()
        fresh_window_w = 727
        fresh_window_h = 500
        fresh_screen_w = self.window.winfo_screenwidth()
        fresh_screen_h = self.window.winfo_screenheight()
        
        x = int((fresh_screen_w / 2) - (fresh_window_w / 2)) + 75
        y = int((fresh_screen_h / 2) - (fresh_window_h / 2)) + 75
        
        fresh_window.title("Untitled")
        fresh_window.geometry(f"{fresh_window_w}x{fresh_window_h}+{x}+{y}")
        fresh_window.grid_rowconfigure(0, weight=1)
        fresh_window.grid_columnconfigure(0, weight=1)
        
        UI(window=fresh_window)
        
    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Document", "*.txt"), ("All Files", "*.*")])

        if file == '':
            return

        with open(file=file, mode="r") as f:
            self.textarea.delete("1.0", END)
            self.window.title(os.path.basename(file))
            self.textarea.insert("1.0", f.read())
    
    def save(self):
        if self.window.title() == "Untitled":
            self.save_as()
        else:
            file_path = self.window.title().strip()
            
            data = self.textarea.get("1.0", END)
            with open(file=file_path, mode="w") as f:
                f.write(data)
                
    def save_as(self):
        file = filedialog.asksaveasfilename(initialfile="*.txt", defaultextension=".txt", filetypes=[("Text Document", "*.txt"), ("All Files", "*.*")])
        
        if file == '':
            return
        
        data = self.textarea.get("1.0", END)
        with open(file=file, mode="w") as f:
            f.write(data)
            self.window.title(os.path.basename(file))

    def page_setup(self):
        pass
    
    def print_content(self):
        pass

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
        if self.current_find_menu_window is not None:
            self.current_find_menu_window.destroy()
        
        self.current_find_menu_window = Toplevel(master=self.window)
        self.current_find_menu_window.title("Find")
        self.current_find_menu_window.resizable(False, False)

        Label(master=self.current_find_menu_window, text="Find what:").grid(row=0, column=0, pady=10)
        Entry(master=self.current_find_menu_window, width=32).grid(row=0, column=1, columnspan=3)
        
        Button(master=self.current_find_menu_window, text="Find Next", width=9).grid(row=0, column=4, padx=5)
        Button(master=self.current_find_menu_window, text="Cancel", width=9).grid(row=1, column=4)
        
        Label(master=self.current_find_menu_window, text="Direction").grid(row=1, column=2)

        radio_btn_var = IntVar()
        Radiobutton(master=self.current_find_menu_window, text="Up", variable=radio_btn_var, value=1).grid(row=2, column=2)        
        Radiobutton(master=self.current_find_menu_window, text="Down", variable=radio_btn_var, value=2).grid(row=2, column=3)
        
        matchcase_var = IntVar()
        wraparnd_var = IntVar()
        Checkbutton(master=self.current_find_menu_window, text="Match case", variable=matchcase_var, onvalue=1, offvalue=2).grid(row=2, column=0)   
        Checkbutton(master=self.current_find_menu_window, text="Wrap around", variable=wraparnd_var, onvalue=1, offvalue=2).grid(row=3, column=0)
        
        self.find_menu_window_opened = True
    
    def select_all(self):
        self.textarea.event_generate("<<SelectAll>>")
    
    def time_date(self):
        current_time = time.strftime("%I:%M %p %d/%b/%Y")
        self.textarea.insert(END, current_time)
    
    # Format menu commands
    def word_wrap(self):
        if self.word_wrap_toggle.get():
            self.textarea.config(wrap=WORD)
            self.scrollbar_x.grid_remove()

        else:
            self.textarea.config(wrap=NONE)
            self.scrollbar_x.grid(row=1, column=0, sticky=EW)
    
    def change_font(self):
        pass
    
    # View menu commands
    # Zoom submenu commands 
    def zoom_in(self):
        self.font['size'] += 2
        
    def zoom_out(self):
        self.font['size'] -= 2
    
    def default_zoom(self):
        self.font['size'] = 16
    
    def status_bar(self):
        if self.status_bar_toggle.get():
            self.status_bar_frame.grid(row=2, column=0, sticky=E)

        else:
            self.status_bar_frame.grid_remove()
            
    # Help menu commands
    def view_help(self):
        webbrowser.open_new_tab("https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA")
    
    def send_feedback(self):
        AppOpener.open("feedback hub")
    
    def about(self):
        messagebox.showinfo(title="About tk Notepad", message="This is an attempt to atleast clone notepad just for fun and test my coding skills in python and playing around in tkinter")