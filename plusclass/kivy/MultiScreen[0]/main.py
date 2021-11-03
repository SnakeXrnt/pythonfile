#------- Import system resource -------
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

#------- Class [main] ---------
class MyApp(App):

	def __init__(self):
		super().__init__()
		self.title = "My Multiple Screen Kivy"

	def build(self):
		return Builder.load_file("index.kv")

	#--------- Changing screen -------
	def to_screen_0(self):
		self.root.current = "Screen0"

	def to_screen_1(self):
		self.root.current = "Screen1"

#------- Trigger ---------
if __name__ == '__main__':
	app = MyApp()
	app.run()

#------- Storage --------
'''
	current: "Screen0"

'''