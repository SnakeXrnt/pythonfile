import tkinter as tk
from page import Page01
from function  import *
from time import *
from page02 import Page02


from settings import Settings
class MainWindow(tk.Tk):

	def __init__(self, App):
		self.settings = App.settings



		super().__init__()
		self.title(self.settings.app_title)
		self.geometry(self.settings.screen)
		self.pages = {}
		self.create_container()
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.logout)

		self.create_page01()
		#self.create_page02()

	