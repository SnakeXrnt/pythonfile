#* untuk dari main ke page.kv harus pakai root, kalau dari page ke main pakai app.

#------------- Import System -------------
from kivy.app import App
from kivy.lang import Builder

#------------- Kivy App -----------------
class KivyApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Using Kivy File"

	def button0_press(self):
		self.root.ids['text_label'].text = self.root.ids['text_input0'].text

	def button1_press(self):
		self.root.ids['text_label'].text = self.root.ids['text_input1'].text

	def build(self):
		return Builder.load_file("page.kv")

#-------------- Runner -----------------
def main():
	app = KivyApp()
	app.run()

#--------------- Trigger ----------------
if __name__ == '__main__':
	main()