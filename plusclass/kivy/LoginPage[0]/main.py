# ------ System resources -----------
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.graphics import Rectangle

from kivy.utils import get_color_from_hex

from kivy.lang import Builder

#----- Color and Font register --------
LabelBase.register(name="Roboto", fn_regular="Roboto-Thin.ttf", fn_bold="Roboto-Medium.ttf")
Window.clearcolor = get_color_from_hex("#101216")

#----- Class ----
class MyApp(App):

	def __init__(self):
		super().__init__()
		self.title = "My App with Screens"

	def build(self):
		return Builder.load_file("index.kv")

	def logger(self):
		username_entry = self.root.screens[0].ids['username_entry'].text
		password_entry = self.root.screens[0].ids['password_entry'].text
		if username_entry == "admin" and password_entry == "admin":
			self.root.current = "HomeScreen"
		else:
			self.root.screens[0].ids['err_msg'].text = "Login Gagal"
			self.root.screens[0].ids['username_entry'].text = ""
			self.root.screens[0].ids['password_entry'].text

#------ Trigger ------
if __name__ == '__main__':
	app = MyApp()
	app.run()

'''
right: self.right
				top: self.top
				canvas:
					Color:
						rgba: from_hex("#fffffff")
					Rectangle:
						pos: self.x, self.top
						size: self.width, self.height
'''