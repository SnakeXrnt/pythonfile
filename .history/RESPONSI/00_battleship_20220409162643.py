import os 
import random

setting_up_board = lambda n : [list("X" * n) for i in range(n)]

def printing_board(board):
    os.system('cls')
    for row in board:
        print (" ".join(row))

a , b , c = input().split()
a , b , c = int(a), int(b), int(c)

a , b , c = list(map(int))
        
def setting_up_ship_location(rows):
    location = [random.randint(0,rows-1),random.randint(0,rows-1)]
    return location

def check_user_input():
    user_input = list(map(int, input("Enter the coordinates(x y): ").split()))
    
    if user_input == my_ship:
        print('You sunk my battleship!')
        return True
    
    my_board[user_input[0]][user_input[1]] = "O"

    return False 
    
        
win = False 
rows = 5
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win: 
    printing_board(my_board)
    print(my_ship)
    win = check_user_input()