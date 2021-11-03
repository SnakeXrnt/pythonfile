from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

import json

LabelBase.register(name='Roboto', fn_regular='assets/font/Roboto-Thin.ttf', fn_bold='assets/font/Roboto-Medium.ttf')

Window.clearcolor = get_color_from_hex("#101216")

class MyApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "My KIVY MD APP"

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/logoutpage.kv"))

		self.my_dict = self.import_user("data.json")

	def build(self):
		self.screen_manager.current = "splash"
		return self.screen_manager

	def on_start(self):
		Clock.schedule_once(self.to_login_page, 5)

	def logger(self):
		username_entry = self.screen_manager.screens[1].ids['username_entry'].text
		password_entry = self.screen_manager.screens[1].ids['password_entry'].text
		if username_entry == self.my_dict["username"] and password_entry == self.my_dict["password"]:
			self.screen_manager.current = "dashboard"
			self.screen_manager.screens[2].ids['username'].text = self.my_dict["username"]
			self.screen_manager.screens[2].ids['nama'].text = self.my_dict["nama"]
			self.screen_manager.screens[2].ids['tanggal'].text = self.my_dict["tanggal"]
			self.screen_manager.screens[2].ids['hobi'].text = self.my_dict["hobi"]
			self.screen_manager.screens[2].ids['postingan'].text = str(self.my_dict["postingan"])
			self.screen_manager.screens[2].ids['pengikut'].text = str(self.my_dict["pengikut"])
			self.screen_manager.screens[2].ids['mengikuti'].text = str(self.my_dict["mengikuti"])
		else:
			pass
			#self.screen_manager.screens[0].ids['err_msg'].text = "Maaf, nama pengguna dan kata sandi tidak cocok."
		self.screen_manager.screens[1].ids['username_entry'].text = ""
		self.screen_manager.screens[1].ids['password_entry'].text = ""

	def to_login_page(self, *args):
		self.screen_manager.current = "login"

	def to_dashboard_page(self, *args):
		self.screen_manager.current = "dashboard"

	def logoutpage(self, *args):
		self.screen_manager.current = "logoutpage"

	def import_user(self, data):
		with open(data, "r") as file:
			diction = json.load(file)
			return diction


if __name__ == '__main__':
	app = MyApp()
	app.run()