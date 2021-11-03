import tkinter as tk

from settings import Settings
from appPage import AppPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings


		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)

		self.create_container()

		self.pages = {}

	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both",expand='True')

	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)



class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()
