#------------- Import System -------------
from kivy.app import App
from kivy.lang import Builder

from kivy.core.text import LabelBase #mengurus untuk semua font

#------------- Registering Font ------------
LabelBase.register(name="Roboto", fn_regular='fonts/Roboto-Thin.ttf', fn_bold='fonts/Roboto-Medium.ttf')

#------------- Clock App -------------
class ClockApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Clock App"

	def build(self):
		return Builder.load_file("page.kv")

#-------------- Runner -----------------
def main():
	app = ClockApp()
	app.run()

#--------------- Trigger ----------------
if __name__ == '__main__':
	main()