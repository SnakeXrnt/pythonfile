from kivymd.app import MDApp
import json
import bcrypt
from
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton

from kivy.config import Config

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder


LabelBase.register(name='Roboto',
					fn_regular='assets/font/Roboto-Thin.ttf',
					fn_bold='assets/font/Roboto-Medium.ttf')

WIDTH = 9*40
HEIGHT = 16*40

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f'{HEIGHT}')
Config.write()

Window.clearcolor = get_color_from_hex("#101216")

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

	
	def logger(self):
		username_entry = self.root.screens[1].ids['username_entry'].text
		password_entry = self.root.screens[1].ids['password_entry'].text
		
		if username_entry in self.users:
			if self.users[username_entry]['password'] == password_entry:
				self.root.screens[1].ids['msg'].text = ''
				self.root.screens[1].ids['username_entry'].text = ''
				self.root.screens[1].ids['password_entry'].text = ''
				self.to_dashboard()
				return True

		self.root.screens[1].ids['msg'].text = 'Login Gagal'
		self.root.screens[1].ids['username_entry'].text = ''
		self.root.screens[1].ids['password_entry'].text = ''


	def load_data(self,file_location):
		try: 
			with open(file_location) as file:
				return json.load(file)
		except:
			return{}

	def build(self):
		self.screen_manager.current = "splash"
		return self.screen_manager

	def on_start(self):
		Clock.schedule_once(self.to_login_page, 3)

	def to_login_page(self, *args):
		self.screen_manager.current = "login"
	
	def to_dashboard(self):
		user= self.current_user
		fullname = self.users[user]['first'].title()+' '+self.users[user]['last'].title()
		bio=self.users[user]['bio']
		pic = 'assets/img/'+self.user[user]['pic']
  
		self.root.screens[2].ids['label_username'].text = user
		self.root.screens[2].ids['label_fullname'].text = fullname
		self.root.screens[2].ids['label_bio'].text = bin
		self.root.screens[2].ids['profile_pic'].source = pic
		self.root.current = 'dashboard'
  
	def close_dialog(self,*args):
		self.dialog_box.dismiss()
		self.root.screen[2].ids['nav_drawer'].set_state('close')
	
	def exit(self,*args):
		self.close_dialog()
		self.current_user = None
		self.root.current = 'login'
  
	def signout(self,*args):
		if not self.dialog_box: 
			self.dialog_box = MDDialog(
				title='Konfirmasi Keluar'
				text = 'Apahkah yakin ingin eluar dari apliaksi ini'
				buttons=[
					MDFlatButton(
						text='Batal'
						on_release=self.close_dialog
         				),
					MDFlatButton(
						text='Ya'
						on_release= self.exit
						)
					
				]
				)
		self.dialog_box.open()
			



if __name__ == '__main__':
	app = MyApp()
	app.run()
 
 
