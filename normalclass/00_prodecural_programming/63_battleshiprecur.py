"""
This program made by : 
Name : Michael jo
class : 10 Kom 2
"""


import os
import random





def intro():
	os.system("cls")
	print("welcome to BattleGround CMD")

	return input("Masukkan berapa ronde yang diinginkan : ")

def setting_up_board(rows):
	
	board = [] #square
	
	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("0")
		board.append(line)

	return board

def setting_up_ship_location(rows):
	location = str(random.randint(0, rows-1)), str(random.randint(0, rows-1))
	return list(location)


def printing_board(board):
	os.system("cls")
	for row in board:
		for item in row:
			print(item, end=" ")
		print()

def check_user_input():
	while True:
		"""
		try:
			user_input = input("Enter skip Location : ").split(" ") # 1 2
			if len(user_input) != 2:
				print(f"You must input 2 integer number!")
				input("ENTER to try Again.")
			else:
				user_input = [str(int(user_input[0])-1), str(int(user_input[1])-1)]
		except ValueError:
			print(f"You must input an integer number!\nPython Error:{e}")
			input("ENTER to try Again.")
		else:
			if len(user_input) != 2:
				pass
			elif user_input[0] < 0 or user_input[0] > rows-1 or user_input[1] < 0 or user_input[1] > rows-1:
				print(f"You must input numbber beetwen 1 and {rows}")
				input("ENTER to try Again.")
			else:
				break
"""
try:
	user_input = input("Enter Ship Location : ").split(" ")
except ValueError as e:
	print(f"You must input an integer number!\nPython Error:{e}")
	input("ENTER to Try Again.")
else:
	if len(user_input) != 2:
		return check_user_input

	if my_ship == user_input:
		return True
	
	my_board[int(user_input[0])][int(user_input[1])] = "X"
	return False

def congrats():
	print(f"You win .... with {attempt} attemps.")

win = False
attempt = 1

rows = intro()
print(rows)
"""
while True:
	try:
		rows= int(intro())
	except ValueError as e:
		print(f"You must input an integer number!\nPython Error:{e}")
		input("ENTER to try Again.")
	else:
		if rows < 3:
			print("You must input a number more than 2.")
			input("ENTER to try Again.")
		else:
			break

my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win:

	printing_board(my_board)
	print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

congrats()