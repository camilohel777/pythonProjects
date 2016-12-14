from random import randint
board = []

for n in range(0,5):
    lst = ["O"] * 5
    board.append(lst)
    
def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board)-1)
    
def random_col(board):
    return randint(0, len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)

print_board(board)
for turn in range(4):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    print ship_row
    print ship_col

    if(guess_row == ship_row and guess_col == ship_col):
        print "Congratulations! You sank my battleship!"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    if turn == 3:
        print "Game Over"
    print "Turn", turn + 1