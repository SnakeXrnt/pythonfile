from kivymd.app import MDApp
import json
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from settings import Settings
from models.user import User

from kivy.config import Config

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

class MyApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "My KIVY MD APP"
	

		self.current_user= None
		self.dialog_box = None

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/passviewer.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/add.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/settings.kv"))

	def build(self):
		self.screen_manager.current = "splash"
		return self.screen_manager

	def on_start(self):
		Clock.schedule_once(self.to_login_page, 3)
  
	def to_login_page(self, *args):
		self.screen_manager.current = "login"
	def to_home_page(self, *args):
		self.screen_manager.current = "dashboard"
	def to_add_page(self, *args):
		self.screen_manager.current = "add"
	def to_settings_page(self, *args):
		self.screen_manager.current = "settings"


	def find_user_by_username(self, username):
		with self.settings.conn:
			self.settings.cur.execute("""
					SELECT * FROM users WHERE username = :username
					""", {"username" : username})
		return self.settings.cur.fetchone()

	def logger(self):
		username_entry = self.root.screens[1].ids['username_entry'].text
		password_entry = self.root.screens[1].ids['password_entry'].text

		user = self.find_user_by_username(username_entry)

		if user:
			if bcrypt.checkpw(password_entry.encode("utf-8"), user[2]):
				self.root.screens[1].ids['msg'].text = ""
				self.root.screens[1].ids['username_entry'].text = ""
				self.root.screens[1].ids['password_entry'].text = ""
				"""
				self.current_user = User(user[1], user[3], user[4], user[5], user[6], user[7])
				self.current_user.id = user[0]
				self.current_user.pic = user[8]
				self.current_user.password = user[2]"""
				self.to_home_page()
				return True
			else:
				print('not ok')

		self.root.screens[1].ids['msg'].text = "Login Gagal"
		self.root.screens[1].ids['username_entry'].text = ""
		self.root.screens[1].ids['password_entry'].text = ""

  

if __name__ == '__main__':
	app = MyApp()
	app.run()
 