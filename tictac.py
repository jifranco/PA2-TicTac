# author: Josue Franco
# date: July 6, 2022
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from board import Board
from player import Player


#driver function
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    player1 = Player("Bob","X")
    player2 = Player("Alice","O")

    turn = True
    while True:
        board.show()
        count = 0
        if turn :
            #check if the cell is empty
            if count == 9:
                break
            count += 1
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True

        if board.isdone():
            break

    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"\n{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"\n{player2.get_name()} is a winner!")
    else:
        print("It is a tie")
    ans = input("Would you like to play again : ").upper()
    if ans == "N":
        break

print("Goodbye")