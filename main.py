'''
This is the main file where we start the chess game.
This file will ask for stdin and print the data to stdout.

For more information please read the README
'''

from player import Player
import globalVar
from chessMoves import *

# Global board variable from board
board = {}
boardHor = globalVar.boardHor
boardVert = globalVar.boardVert

# Create the players
white = Player("w", [], [], [], [], [], [])
black = Player("b", [], [], [], [], [], [])

'''
Sumamry:
Verify the number of pieces entered are valid

Input:
piece: String to determine which piece
number: Number of pieces entered

Output:
Boolean: To determine was the data valid
'''
def checkNumPieces(piece, number):
   # Verify the number of pieces are correct
   if(piece == "pawn" and number > 8):
      print("Too many pawns. Please enter again.")
      return False
   elif(piece == "rook" and number > 2):
      print("Too many rooks. Please enter again.")
      return False
   elif(piece == "knight" and number > 2):
      print("Too many knight. Please enter again.")
      return False
   elif(piece == "bishop" and number > 2):
      print("Too many bishop. Please enter again.")
      return False
   elif(piece == "queen" and number > 1):
      print("Too many queen. Please enter again.")
      return False
   elif(piece == "king" and number > 1):
      print("Too many king. Please enter again.")  
      return False
   # If everything is fine, proceed   
   return True

'''
Summary:
Insert the piece into the board[hor][vert] and store into player class

Input:
piece: String to determine which array to store in Player
hor: The string number associated with the y axis
vert: The string letter associated with the x axis
player: Player currently looking at
'''
def insertBoard(piece, hor, vert, player):
   position = vert + hor
   name = player.name

   # Put the correct name on board
   if(piece == "pawn"):
      board[hor][vert] = name + "p"
      print(name + "p inserted in [" + vert + "," + hor +"]")
      player.pawn.append(position)
   elif(piece == "rook"):
      board[hor][vert] = name + "r"
      print(name + "r inserted in [" + vert + "," + hor +"]")
      player.rook.append(position)
   elif(piece == "knight"):
      board[hor][vert] = name + "k"
      print(name + "k inserted in [" + vert + "," + hor +"]")
      player.knight.append(position)
   elif(piece == "bishop"):
      board[hor][vert] = name + "b"
      print(name + "b inserted in [" + vert + "," + hor +"]")
      player.bishop.append(position)
   elif(piece == "queen"):
      board[hor][vert] = name + "Q"
      print(name + "Q inserted in [" + vert + "," + hor +"]")
      player.queen.append(position)
   elif(piece == "king"):
      board[hor][vert] = name + "K"
      print(name + "K inserted in [" + vert + "," + hor +"]")
      player.king.append(position)

'''
Summary: 
The array with the list of character from the user. If the position format is valid,
call insert function to insert into board.

Input:
piece: String we are currently looking at, such as pawn
arr: Array with a list of input from the user
player: Player to insert the pieces into

Output:
False: Data entered is invalid
True: Data is valid and inserted into board
'''
def parseLine(piece, arr, player):
   # if empty, means no input
   if(len(arr) == 0):
      return True

   # if the length is not correct, ask for another input
   if(not checkNumPieces(piece, len(arr))):
      return False

   # Flag variable
   continued = 0
   # Check for valid format from the user      
   for i in range(len(arr)):
      if(len(arr[i]) != 2):
         print("Invalid Format: " + arr[i] + ". Please enter again.")
         continued = 1
         continue
      elif(arr[i][0] < 'a' or arr[i][0] > 'h'):
         print("Invalid Character: " + arr[i][0] + " in " + arr[i] + ". Please enter again.")
         continued = 1
         continue
      elif(arr[i][1] < '1' or arr[i][1] > '8'):
         print("Invalid Number: " + arr[i][1] + " in " + arr[i] + ". Please enter again.")
         continued = 1
         continue
      else:
         hor = arr[i][1]
         vert = arr[i][0]
         # Check to see if board is empty
         if board[hor][vert]:
            print("The coordinate ["+ vert + "," + hor +"] for " + piece + " is already taken. Please enter again.")
            continued = 1
            continue

         # Put the pieces on the board
         insertBoard(piece, hor, vert, player)

   # if any skipped ask for another input
   if(continued == 1):
      return False      
   return True

'''
Summary:
Request string from stdin and parse the string by space character.

Input:
player: Player to store the stdin into
'''
def piecePosition(player):
   name = player.name

   # Get positions from stdin for chess positions. If format is invalid, ask again
   while True:
      pawn = raw_input("Pawn position:")
      pawn = pawn.split()
      if(parseLine("pawn", pawn, player)):
         break
   while True:
      rook = raw_input("Rook position:")
      rook = rook.split()
      if(parseLine("rook", rook, player)):
         break  
   while True:   
      knight = raw_input("Knight position:")
      knight = knight.split()
      if(parseLine("knight", knight, player)):
         break
   while True:   
      bishop = raw_input("Bishop position:")
      bishop = bishop.split()
      if(parseLine("bishop", bishop, player)):
         break
   while True:
      queen = raw_input("Queen position:")
      queen = queen.split()
      if(parseLine("queen", queen, player)):
         break
   while True:
      king = raw_input("King position:")
      king = king.split()
      if(parseLine("king", king, player)):
         break
   return

'''
Summary: 
Prints the current chess board to stdout
'''
def printBoard():
   print("The current chess board looks like:")
   for i in range(boardVert, 0, -1):
      for letter in boardHor:
         value = board[str(i)][letter]
         if not value:
            print("{  }"),
         else:
            print("{" + str(value) + "}"),
      print("");      
   return

'''
Summary:
Prints all the possible moves based on the number of pieces the player has.

Input:
player: Player to look at with the pieces
'''
def playerMoves(player):
   playerPrint = "Player "
   if(player.name == "w"):
      playerPrint += "White "
   else:
      playerPrint += "Black "
   playerPrint += "list of all possible moves:"
   print(playerPrint)

   pawn = pawnMoves(board, player)
   if(pawn != ""):
      print(pawn)
   # Rook Movement
   rook = rookMoves(board, player)
   if(rook != ""):
      print(rook)
   # Knight Movement
   knight = knightMoves(board, player)
   if(knight != ""):
      print(knight)
   # Bishop Movement
   bishop = bishopMoves(board, player)
   if(bishop != ""):
      print(bishop)
   # Queen Movement
   queen = queenMoves(board, player)
   if(queen != ""):
      print(queen)
   # King Movement
   king = kingMoves(board, player)
   if(king != ""):
      print(king)
   return

'''
Summary:
Ask user from stdin for which player's move to show. If data is invalid as again.
'''
def playerTurns():
   turn = raw_input("Please enter which player's turn to take (White/Black/Both): ")
   turnLower = turn.lower()
   if(turnLower == "white"):
      playerMoves(white)
   elif(turnLower == "black"):
      playerMoves(black)
   elif(turnLower == "both"):
      playerMoves(white)
      print("")
      playerMoves(black)
   else:
      print("Invalid Input: " + turn + "Please enter again.")
      playerTurns()

'''
Summary:
Create the two dimensional board from a1 to h8
'''
def createBoard():
   for i in range(boardVert, 0, -1):
      board[str(i)] = {}
      for letter in boardHor:
         board[str(i)][letter] = {}

# Start the main
createBoard()
# start the input for player white
print("Please Enter piece position for player White (format: a1 d4 f2):")
piecePosition(white)
print("")
# start the input for player black
print("Please Enter piece position for player Black (format: a1 d4 f2):")
piecePosition(black)
print("")
# print the board to show user what was inserted
printBoard()
print("")
# determine which players turn to show
playerTurns()
print("")
