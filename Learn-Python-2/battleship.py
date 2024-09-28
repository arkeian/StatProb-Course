# Page 1
"""
(ID) Tidak ada kode yang disertakan di dalam Page 1 karena belum diinstruksikan untuk membuat sebuah blok kode.
(EN) No codes are included within Page 1 because this page has yet to give the learner any instructions.
"""

# Page 2 - 4
board = []
for _ in range(5):
    board.append(["O"] * 5)

print(board)

# Page 5
board = []
for _ in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(row)

print_board(board)

# Page 6
board = []
for _ in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

# Page 7
from random import randint

board = []
for _ in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

random_row(board)
random_col(board)

# Page 8 - 19
from random import randint

board = []
for _ in range(5):
  board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

for turn in range(4):
    print(f"Turn {turn + 1}")
    print_board(board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print("Game Over")