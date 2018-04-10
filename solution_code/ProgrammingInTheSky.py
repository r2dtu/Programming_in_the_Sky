from random import *

# the tic tac toe board
board = [
          ["_","_","_"],
          ["_","_","_"],
          ["_","_","_"]
        ]

def printBoard():
  '''
  print the board with updated pieces
  '''
  print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
  print('-----------')
  print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
  print('-----------')
  print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    
def isWon(player):
  '''
  check if the player has won the game by checking each row, col and diagonal
  return True if the player wins the game, False otherwise.
  '''
  for i in range(3):
    if board[i][0] == player and board[i][1] == player and board[i][2] == player:
      return True
  
  for i in range(3):
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return True
          
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  
  return False

def validMove(row, col):
  '''
  check the given row and col is valid - no piece on that square
  return True if the given square is "_" meaning no piece occupied it
  False otherwise.
  '''
  return board[row][col] is "_"

def humanTurn( symbol ):
  '''
  human's turn. The command line will ask you to input a row and a col
  Then it will check whether the square has already been occupied. If yes,
  it will ask you again to input another row and col.
  If it is valid, it will place your piece onto the board and print it.
  It also checks whether you wins the game if you place your piece in that 
  square.

  Return True if you wins the game. False otherwise.
  '''
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
  '''
  computer's turn. It will generate random move for the computer.
  If the move valid, it will place the piece onto the board and print it.
  It also checks whether computer wins the game 

  Return True if computer wins the game. False otherwise.
  '''
  row = randint(0, 2)
  col = randint(0, 2)
  while( validMove(row, col) is False ):
    row = randint(0, 2)
    col = randint(0, 2)
  
  print("My move is {} {}".format(row, col))
  board[row][col] = symbol
  printBoard()
  if isWon(symbol):
    print("I won!")
    return True
  else:
    return False

def humanFirst():
  '''
  if human goes first, then loop human and computer turns and 
  constantly check if the return is True - meaning that the game is over.
  '''
  for i in range(4):
    if humanTurn("x") is True:
      break
    if computerTurn("o") is True:
      break
  else:
    if humanTurn("x") is False:
      print("A tie!")

def computerFirst():
  '''
  if computer goes first, then loop human and computer turns and 
  constantly check if the return is True - meaning that the game is over.
  '''
  computerTurn("x")
  for i in range(4):
    if humanTurn("o") is True:
      break
    if computerTurn("x") is True:
      break
  else:
    print("A tie!")

def main():
  '''
  generate random number between 0 and 1
  if it is 0 then human goes first
  otherwise computer goes first
  '''
  move = randint(0,1)
  if move is 0:
    print("You start first. You get x and I get o")
    humanFirst()
  else:
    print("I start first. I get x and you get o")
    computerFirst()

main()