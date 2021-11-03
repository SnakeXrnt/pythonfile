import tkinter as tk

from config import Config
from board import Board


class Window(tk.Tk):

	def __init__(self, Game):
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()


	def create_container(self):
		self.containter = tk.Frame(self, bg="white")
		self.containter.pack(fill="both", expand=True)

	def create_board(self):
		self.pages['board'] = Board(self.containter, self)


class Battleship:

	def __init__(self):
		self.config = Config()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()