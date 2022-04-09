import os 
import random

setting_up_board = lambda n : [["X"] * n for i in range(n)]

def printing_board(board):
    os.system('cls')
    for row in board:
        print (" ".join(row))
        
def setting_up_ship_location(rows):
location = [random.radint(0,rows-1),random.radint(0,rows-1)]
    
        
win = False 
rows = 5
my_board = setting_up_board(rows)

while not win: 
    printing_board(my_board)
    input()