#kivyEnv\Scripts\activate -> activate environment

#------------- Import System -------------
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#------------- First App -----------------
class FirstApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Hello First App"

	def button0_press(self, button_pressed):
		self.text_label.text = self.text_input0.text

	def button1_press(self, button_pressed):
		self.text_label.text = self.text_input1.text

	def build(self):
		text_label = Label(text="Waiting for Button Press")

		button0 = Button(text="Click Me")
		button1 = Button(text="Click Me")

		text_input0 = TextInput(text="Text Input")
		text_input1 = TextInput(text="Text Input")

		boxlayout_h0 = BoxLayout(orientation="horizontal")
		boxlayout_h1 = BoxLayout(orientation="horizontal")

		main_boxlayout = BoxLayout(orientation="vertical")

		boxlayout_h0.add_widget(widget=text_input0)
		boxlayout_h0.add_widget(widget=button0)

		boxlayout_h1.add_widget(widget=text_input1)
		boxlayout_h1.add_widget(widget=button1)

		main_boxlayout.add_widget(widget=text_label)
		main_boxlayout.add_widget(widget=boxlayout_h0)
		main_boxlayout.add_widget(widget=boxlayout_h1)

		return main_boxlayout

#-------------- Runner -----------------
def main():
	app = FirstApp()
	app.run()

#--------------- Trigger ----------------
if __name__ == '__main__':
	main()
