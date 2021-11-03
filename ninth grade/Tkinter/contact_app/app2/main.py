import tkinter as tk
from tkinter import Menu

from settings import Settings
from appPage import AppPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(False, False)

		self.create_menu()
		self.create_container()

		self.pages = {}
		self.create_page()

	def create_menu(self):
		pass

	def create_container(self):
		self.container = tk.Frame(bg="grey")
		self.container.pack(side='top', fill='both', expand=True)

	def create_page(self):
		self.pages['first'] = AppPage(self.container, self.app)

	def update_frame(self):
		self.pages['first'].update_content.tkraise()

class ContactApp:

	def __init__(self):
		self.settings = Settings()

		self.contact = Window(self)

	def run(self):
		self.contact.mainloop()

if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()