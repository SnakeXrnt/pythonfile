from kivymd.app import MDApp
import json
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton

from kivy.config import Config

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

class MyApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "My KIVY MD APP"

		self.users= self.load_data('data/users.json')
		self.current_user= None
		self.dialog_box = None

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))
  		self.screen_manager.add_widget(Builder.load_file("pages/pass.kv"))