import tkinter as tk
from PIL import Image, ImageTk


class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.board = []
		self.game = Game
		self.config = Game.config
		self.row = self.config.row
		self.column = self.config.column

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		#CONFIG BUTTON
		#self.buttonPixelVirtual = tk.PhotoImage(width=1, height=1)


		self.create_main_frame()
		self.update_board()


	def update_board(self):
		self.create_board()
		self.show_board()
		self.create_button_board()
		self.show_button_board()


	def create_main_frame(self):
		self.main_frame = tk.Frame(self, height=self.config.side, width=self.config.side, bg="black")
		self.main_frame.pack(expand=True)


	def create_board(self):
		self.frame_rows = [] #[0,1,2,3,4]
		colors = ["yellow", "green", "cyan", "orange", "magenta"]

		nRow, nColumn = self.config.row, self.config.column
		row_height, row_width = self.config.side//nRow, self.config.side

		for i in range(nRow):
			frame = tk.Frame(self.main_frame, height=row_height, width=row_width, bg=colors[i])
			self.frame_rows.append(frame)

	def show_board(self):
		for frame in self.frame_rows:
			frame.pack()

	def create_button_board(self):
		self.button_board = []

		nRow, nColumn = self.config.row, self.config.column
		button_height, button_width = self.config.side//nRow-10, self.config.side//nColumn-10

		image = Image.open(self.config.init_img)
		image_w , image_h = image.size
		ratio = image_w/button_width
		new_size = (int(image_w//ratio//2), int(image_h//ratio//2))
		image = image.resize(new_size)
		self.init_img_btn = ImageTk.PhotoImage(image)

		image2 = Image.open(self.config.final_img)
		image_w , image_h = image2.size
		ratio = image_w/button_width
		new_size = (int(image_w//ratio//4), int(image_h//ratio//4))
		image2 = image2.resize(new_size)
		self.final_img_btn = ImageTk.PhotoImage(image2)
		for i in range(nRow):
			row = []

			for j in range(nColumn):
				button = tk.Button(self.frame_rows[i], bg="purple", image=self.init_img_btn, height=button_height, width=button_width,command=lambda x=i,y=j:self.clicked(x,y))
				row.append(button)

			self.button_board.append(row)

	def show_button_board(self):
		nRow, nColumn = self.config.row, self.config.column
		for i in range(nRow):
			for j in range(nColumn):
				self.button_board[i][j].pack(side="left")

	def clicked(self,pos_x,pos_y):

		print(pos_x, pos_y)
		self.button_board[pos_x][pos_y].configure(image=self.final_img_btn)
