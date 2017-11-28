# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:19:41 2017

@author: Ethan
"""
from random import randint

board = []
for i in range(5):
    board.append(['O', 'O', 'O', 'O', 'O'])
print(board)

def print_board(board_in):
    for row in board_in:
        print(" ".join(row))
        
print_board(board)

def random_row(board_in):
    return(randint(0, len(board_in) - 1))
    
def random_col(board_in):
    return(randint(0, len(board_in) - 1))


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! you sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print_board(board)        
    if turn == 3:
        print("Game Over")
