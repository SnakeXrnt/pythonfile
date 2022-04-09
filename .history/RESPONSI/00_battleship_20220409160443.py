import os 

setting_up_board = lambda n : [["O"] * n for i in range(n)]

def printing_board(board):
    os.system('cls')
    for row in board:
        print (" ".join(row))
        
def setting_up_ship_location 