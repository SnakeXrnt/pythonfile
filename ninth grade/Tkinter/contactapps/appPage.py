import tkinter as tk

class AppPage(tk.Frame):

    def __init__(self, parent , App):

        self.app = App
        self.settings = App.settings

        super().__init__(parent)
