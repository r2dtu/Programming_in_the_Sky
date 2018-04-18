"""
File: 		TicTacToe.py
Description: 	Part of the IEEExHKN Programming in the Sky Workshop on April
		22, 2018. This file runs a Tic Tac Toe game, where a player
		will play against an automated computer player.
Editor:		<YOUR NAME>
"""

from random import *

# the tic tac toe board
board = [
		["_","_","_"],
		["_","_","_"],
		["_","_","_"]
	]

def printBoard():
	"""
	Description:	Print the board with updated pieces.
	"""

        #TODO Modify the code below so that the actual values of the board
        #     are printed

        print(' ' + ' | ' + ' | ')
	print('-----------')
	print(' ' + ' | ' + ' | ' )
	print('-----------')
	print(' ' + ' | ' + ' | ' )


def isWon(player):
	"""
	Parameters:	player - x or o, indicating which character to check
	Description:	Checks if the player has won the game. This is done by
			checking each row, col and diagonal.
	Returns:	True if the player wins the game, False otherwise.
	"""

        

def validMove(row, col):
	"""
	Description: check the given row and col is valid - no piece on that square
	return True if the given square is "_" meaning no piece occupied it
	False otherwise.
	"""

def humanTurn( symbol ):
	"""
	Parameters:	symbol - which character to display for the human
	Description: 	Executes the human's turn. The command line will ask
			you to input a row and a column. Then it will check whether 
			the square has already been occupied. If yes, it will ask 
			you again to input another row and col. If it is valid, it 
			will place your piece onto the board and print it. It also 
			checks whether you wins the game if you place your piece in 
			that square.
	Returns:	True if you win the game. False otherwise.
	"""
	row, col = input("Enter your move: (row column):").split()
	row = int(row)
	col = int(col)
	while( validMove(row, col) is False ):
		print("Sorry that cell is already occupied. Please try again.")
		row, col = input("nEnter your move: (row column):").split()
		row = int(row)
		col = int(col)

	board[row][col] = symbol
	printBoard()

	if isWon(symbol):
		print("You Won!")
		return True
	else:
		return False


def computerTurn( symbol ):
	"""
	Parameters:	symbol - which character to display for the human
	Description:	Executes the computer's turn. It will generate a random 
			move for the computer. Just like with the human move,
			if the move is valid, it will place the piece onto the 
			board and print it. It also checks whether computer wins 
			the game.

	Returns:	True if the computer wins the game. False otherwise.
	"""

def humanFirst():
	"""
	Description:	Called if the human player goes first. Loop between human 
			and computer turns and constantly check if the return
			value from those is True, signifying that the game is over.
	"""
	for i in range(4):
		if humanTurn("x") is True:
			break
		if computerTurn("o") is True:
			break
	else:
		if humanTurn("x") is False:
			print("A tie!")


def computerFirst():
	"""
	Description:	Called if the computer player goes first. Loop between 
			human and computer turns and constantly check if the 
			return value from those is True, signifying that the game 
			is over.
	"""
	computerTurn("x")
	for i in range(4):
		if humanTurn("o") is True:
			break
		if computerTurn("x") is True:
			break
	else:
		print("A tie!")


def main():
	"""
	Description:	Runs the main program. Determines whether the human or
			computer player goes first by generating a random number 
			between 0 and 1. If it is 0, then human goes first,
			otherwise the computer player goes first.
	"""
	move = randint(0,1)
	if move is 0:
		print("You start first. You get x and I get o")
		humanFirst()
	else:
		print("I start first. I get x and you get o")
		computerFirst()

# Run the Tic-Tac-Toe program
main()
