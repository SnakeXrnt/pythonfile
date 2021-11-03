
class Settings:

	def __init__(self):

		#App Conf
		self.title = "Contact"


		#Window Conf
		base = 75
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+500+500"