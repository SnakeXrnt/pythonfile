import os 

setting_up_board = lambda n : [["O"] * n for i in range(n)]

def printing_board(board):
    os.system('cls')
    for row in board:
        print (" ".join(row))
        
