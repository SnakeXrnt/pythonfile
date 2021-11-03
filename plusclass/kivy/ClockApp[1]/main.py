'''
1. sudo apt install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

Topic: Kelas Komputer
Time: This is a recurring meeting Meet anytime

Join Zoom Meeting
https://us02web.zoom.us/j/83790199868?pwd=TUR6UXB4OWtzZ3MxTDAwQkNSVitOZz09

2. apt - get update kalau perlu
3. aktifin kivyEnv
4. pip install buildozer
5. masuk ke folder project
6. buildozer init
7. ubah info di buildozer spec lihat dari home

yang diubah itu package.name, title, requirement , orientation, buat fullscreen = 1 untuk fullscreen, permision -> untuk yang import, log.cat hapus saja # nya

8. di hp masuk ke settings -> about phone -> version -> klik 10 kali build number -> masukin password -> sambungkan hp ke laptop dengan sambungan usb
9. tulis buildozer android debug deploy run -> di terminal

'''
#------------- Import System -------------
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.core.text import LabelBase

#------------- Registering Font ------------
LabelBase.register(name="Roboto", fn_regular="Roboto-Thin.ttf", fn_bold="Roboto-Medium.ttf")

#------------- Clock App -------------
class ClockApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Clock App"

		self.stopwatch_started = False

	def update_clock(self, *args):
		time = datetime.now()
		self.root.ids['time'].text = time.strftime("[b]%H[/b]:%M:%S")
		self.update_stopwatch()

	def update_stopwatch(self):
		if self.stopwatch_started:
			time = datetime.now() - self.stopwatch_time_start
			time = str(time)[0:10]
			self.root.ids['stopwatch'].text = f"{time[2:8]}[size=40]{time[8:10]}[/size]"


	def start_stop(self):
		text = "Start"
		if not self.stopwatch_started:
			self.stopwatch_time_start = datetime.now()
			text = "Stop"
		self.root.ids['start_stop'].text = text
		self.stopwatch_started = not self.stopwatch_started


	def reset(self):
		if self.stopwatch_started:
			self.root.ids['start_stop'].text = 'Start'
			self.stopwatch_started = False
		self.root.ids['stopwatch'].text = "00:00.[size=40]00[/size]"

	def on_start(self):
		clock_trigger = Clock.schedule_interval(self.update_clock, 1/60)

	def build(self):
		return Builder.load_file("page.kv")

#-------------- Runner -----------------
def main():
	app = ClockApp()
	app.run()

#--------------- Trigger ----------------
if __name__ == '__main__':
	main()