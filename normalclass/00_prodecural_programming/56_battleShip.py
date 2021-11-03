"""
This program made by:
Name:Michael jo
Class:10Komp2
"""

import os
import random

def intro():
	os.system("cls")
	print("Welcome to Battleroyale CMD")

	return input("Masukkin jumlah attempt yang diinginkan : ")
	
def setting_up_board(rows):
	
	board = []

	for now in range(rows):
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

	user_input = input("Enter Ship Location : ").split(" ")
	user_input = [int(user_input[0])-1, int(user_input[1])-1]
	if my_ship == user_input:
		return True

	my_board[int(user_input[0])][int(user_input[1])] = "X"
	return False

def congrats():
	print(f"Kamu menang .... dengan {attempt} attempts.")

win = False
attempt = 1

rows = int(intro())
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win:

	printing_board(my_board)
	print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

Selamat ()
