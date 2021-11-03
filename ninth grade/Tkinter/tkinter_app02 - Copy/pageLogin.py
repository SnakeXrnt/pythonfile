import tkinter as tk

from PIL import Image, ImageTk

class PageLogin(tk.Frame):

    def __init__(self,parent,App):
        self.application = App
        self.setting = App.settings

        super().__init__(parent)
        self.configure(bg="grey")
        self.grid(row=0,column=0 , sticky='nsew')
        parrent.grid_columnconfigure(0,weight=1)
        parrent.grid_rowconfigure(0,weight=1)

        self.main_frame = tk.Frame(self,height = self.settings.height , width=self.setting.width , bg='blue')
        self.main_frame.pack(expand=True)

        self.btn_login = tk.Button(self.main_frame,text="LOGIN")
        self.btn_login.pack(pady=10)

        self.btn_login2 = tk.Button(self.main_frame,text="LOGIN")
        self.btn_login2.pack(pady=10)
