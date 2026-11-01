from random import randint

board = []
for x in range(5):
    board.append(["O"] * 5)

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)