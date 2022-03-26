
def setting_up_board():
    return ['x'*3 for _ in range (3)]

def printing_board(board):
    for row in board:
        print(' '.join(row))

win = False
row = 5
my_board = setting_up_board()

print(my_board)