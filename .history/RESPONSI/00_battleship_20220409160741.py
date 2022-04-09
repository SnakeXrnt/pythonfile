import os 
import random

setting_up_board = lambda n : [["x"] * n for i in range(n)]

def printing_board(board):
    os.system('cls')
    for row in board:
        print (" ".join(row))
        
win = False 
rows = 5
my_board = setting_up_board(rows)
my_ship = lambda rows :[random.radint(0,rows-1),random.radint(0,rows-1)]

while not win: 
    printing_board(my_board)
    input()