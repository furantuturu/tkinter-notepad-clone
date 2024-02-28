from tkinter import *

class FindWindowUI:
    def __init__(self, find_window, textarea) -> None:
        self.find_window = find_window      
        self.textarea = textarea
        
        Label(master=self.find_window, text="Find what:").grid(row=0, column=0, pady=10)
        self.textentry = Entry(master=self.find_window, width=32)
        self.textentry.grid(row=0, column=1, columnspan=3)
        
        Button(master=self.find_window, text="Find Next", width=9, command=self.find_next).grid(row=0, column=4, padx=5)
        Button(master=self.find_window, text="Cancel", width=9).grid(row=1, column=4)
        
        Label(master=self.find_window, text="Direction").grid(row=1, column=2)

        radio_btn_var = IntVar()
        Radiobutton(master=self.find_window, text="Up", variable=radio_btn_var, value=1).grid(row=2, column=2)        
        Radiobutton(master=self.find_window, text="Down", variable=radio_btn_var, value=2).grid(row=2, column=3)
        
        matchcase_var = IntVar()
        wraparnd_var = IntVar()
        Checkbutton(master=self.find_window, text="Match case", variable=matchcase_var, onvalue=1, offvalue=2).grid(row=2, column=0)   
        Checkbutton(master=self.find_window, text="Wrap around", variable=wraparnd_var, onvalue=1, offvalue=2).grid(row=3, column=0)
        
    def find_next(self):
        # text_index = self.textarea.search(self.textentry.get(), "1.0", END, True)
        # print(text_index)
        # if text_index is not None:
        #     self.textarea.tag_add("highlight", text_index, END)
        #     self.textarea.tag_config("hightlight", background="blue")
        pass