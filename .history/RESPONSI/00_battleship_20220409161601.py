import os 
import random

setting_up_board = lambda n : [["X"] * n for i in range(n)]

def printing_board(board):
    os.system('cls')
    for row in board:
        print (" ".join(row))
        
def setting_up_ship_location(rows):
    location = [random.radint(0,rows-1),random.radint(0,rows-1)]
    return location

def check_user_input():
    user_input = list(map(int, input("Enter the coordinates(x y): ").split()))
    
    if user)
    
        
win = False 
rows = 5
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win: 
    printing_board(my_board)
    print(my_ship)
    input()
    win = check_user_input()