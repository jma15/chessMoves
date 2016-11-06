# This file calculates the possible moves of each piece

import globalVar

# Global board variable from board
boardHor = globalVar.boardHor
boardVert = globalVar.boardVert

'''
Summary:
Check the board to see if the spot is empty or not. Returns the first character if not empty,
which is the player's name

Input:
board: Two dimensional map holding all the pieces positions
hor: String that should be a number for the y axis
vert: String that should be letter for the x axis

Output:
False: If the board is empty
'w': returns 'w' if the board[hor][vert] is own by player white
'b': returns 'b' if the board[hor][vert] is own by player black
'''
def checkBoard(board, hor, vert):
   # if not exist return false, else return first character
   if not board[hor][vert]:
      return False
   return board[hor][vert][0]

'''
Summary:
Main function for all the pieces (except pawns) to determine which position they can move to.
It takes the current give position [num][let] and add the offset to the position. [num + offSetNum][let + offSetLet]
This will repeat until the the new position is outofbound OR if there is a limit value.

There are conditions to handle for the logic:
1. If the position is empty, add the position to the array and continue
2. If the position is owned by current player, means there is another piece owned by the player
      which is blocking the current piece, so we can stop
3. If the position is owned by other player, means we can take over that position and stop

Input:
board: Two dimensional map holding all the pieces positions
let: String that should be letter for the x axis
num: String that should be a number for the y axis
player: Player who holds the pieces
offSetNum: Int to increase the num by
offSetLet: Int to increase the let by
limit: Int to control the outofbound loop, if negative given means loop until out of bound

Output:
tempArray: Array with all possible position for the piece to move to
'''
def offSet(board, let, num, player, offSetNum, offSetLet, limit):
   # Base case if limit is 0, means dont run
   if(limit == 0):
      return []
   tempArray = []
   index = boardHor.index(let)
   tempNum = int(num) + offSetNum
   tempLet = index + offSetLet
   curLimit = 1

   # Loop until an edge, or if limit is reached
   while(tempNum <= boardVert and tempNum >= 1 and tempLet < boardVert and tempLet >= 0):
      curLetter = boardHor[tempLet]
      pos = curLetter + str(tempNum)
      if(checkBoard(board, str(tempNum), curLetter) == False):
         tempArray += [pos]
      elif(checkBoard(board, str(tempNum), curLetter) == player.name):   
         break
      else:
         tempArray += [pos]
         break

      tempNum += offSetNum
      tempLet += offSetLet
      # This is to limit the number of runs
      if(limit == curLimit):
         break
      curLimit += 1
   return tempArray

'''
Summary:
Similar to offSet() function, but requires different check algorithm.

There are conditions to handle for the logic:
condition "front": This is to check the position in front of the pawn. If is any pieces
   in front, the pawn cannot move, else this can move front by one or two spot (only two spots if it did not move)
condition "side": This is to check the position one diagonal in front of the pawn. If there is a piece
   owned by another player, then add the position to the array else do not add.

Input:
board: Two dimensional map holding all the pieces positions
let: String that should be letter for the x axis
num: String that should be a number for the y axis
player: Player who holds the pieces
offSetNum: Int to increase the num by
offSetLet: Int to increase the let by
limit: Int to control the outofbound loop, if negative given means loop until out of bound
flag: String to determine which check to perform

Output:
tempArray: Array with all possible position for the piece to move to
'''
def offSetPawn(board, let, num, player, offSetNum, offSetLet, limit, flag):
   # Base case if limit is 0, means dont run
   if(limit == 0):
      return []
   tempArray = []
   index = boardHor.index(let)
   tempNum = int(num) + offSetNum
   tempLet = index + offSetLet
   curLimit = 1

   # Loop until an edge, or if limit is reached
   while(tempNum <= boardVert and tempNum >= 1 and tempLet < boardVert and tempLet >= 0):
      curLetter = boardHor[tempLet]
      pos = curLetter + str(tempNum)
      # Only add if the position in front is empty
      if(checkBoard(board, str(tempNum), curLetter) == False and flag == "front"):
         tempArray += [pos]
      # Only add if there is opponent piece on the side
      elif(checkBoard(board, str(tempNum), curLetter) != False and checkBoard(board, str(tempNum), curLetter) != player.name 
            and flag == "side"):
         tempArray += [pos]
      else:
         break

      tempNum += offSetNum
      tempLet += offSetLet
      # This is to limit the number of runs
      if(limit == curLimit):
         break
      curLimit += 1
   return tempArray

'''
Summary:
Helper function to find all diagonal movements for pieces (bishop, king, queen).
The diagonal requires offset to 
move up one and right one, 
move up one and left one,
move down one and right one,
move down one and left oen

Input:
board: Two dimensional map holding all the pieces positions
let: String that should be letter for the x axis
num: String that should be a number for the y axis
player: Player who holds the pieces
limit: Int to control the outofbound loop, if negative given means loop until out of bound

Output:
tempArray: Array with all possible position for the piece to move to
'''
def diagMove(board, let, num, player, limit):
   tempArray = []
   index = boardHor.index(let)
   tempNum = int(num) + 1
   tempLet = index + 1
   offSetArr = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
   for i in range(len(offSetArr)):
      tempArray += offSet(board, let, num, player, offSetArr[i][0], offSetArr[i][1], limit)

   return tempArray

'''
Summary:
Helper function to find all horizontal and vertical movements for pieces (rook, king, queen).
The horizontal requires offset:
move up zero and right one, 
move up zero and left one

The vertical requires offset:
move down one and right zero,
move down one and left zero

Input:
board: Two dimensional map holding all the pieces positions
let: String that should be letter for the x axis
num: String that should be a number for the y axis
player: Player who holds the pieces
limit: Int to control the outofbound loop, if negative given means loop until out of bound

Output:
tempArray: Array with all possible position for the piece to move to
'''
def horVertMove(board, let, num, player, limit):
   tempArray = []
   offSetArr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

   for i in range(len(offSetArr)):
      tempArray += offSet(board, let, num, player, offSetArr[i][0], offSetArr[i][1], limit)

   return tempArray

'''
Summary:
Loop through the rook array in player class and find the possible moves.

Input:
board: Two dimensional map holding all the pieces positions
player: Player who holds the pieces

Output:
resultString: Returns the string with all possible positons
'''
def rookMoves(board, player):
   resultString = ""
   # find the rook pieces location
   for i in range(len(player.rook)):
      position = player.rook[i]
      let = position[0]
      num = position[1]
      tempString = "Rook [" + let + "," + num + "]: "
      # get all the possible moves for rooks
      arr = horVertMove(board, let, num, player, -1)
      arr.sort()
      tempString += " ".join(arr)
      resultString += tempString + "\n"      
   return resultString.strip()

'''
Summary:
Loop through the knight array in player class and find the possible moves.

Input:
board: Two dimensional map holding all the pieces positions
player: Player who holds the pieces

Output:
resultString: Returns the string with all possible positons
'''
def knightMoves(board, player):
   resultString = ""
   offSetArr = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

   # find the knight pieces location
   for i in range(len(player.knight)):
      tempArray = []
      position = player.knight[i]
      let = position[0]
      num = position[1]
      tempString = "Knight [" + let + "," + num + "]: "
      # get all the possible moves for knight
      for i in range(len(offSetArr)):
         tempArray += offSet(board, let, num, player, offSetArr[i][0], offSetArr[i][1], 1)

      tempArray.sort()
      tempString += " ".join(tempArray)
      resultString += tempString + "\n"
   return resultString.strip()

'''
Summary:
Loop through the bishop array in player class and find the possible moves.

Input:
board: Two dimensional map holding all the pieces positions
player: Player who holds the pieces

Output:
resultString: Returns the string with all possible positons
'''
def bishopMoves(board, player):
   resultString = ""
   # find the bishop pieces location
   for i in range(len(player.bishop)):
      position = player.bishop[i]
      let = position[0]
      num = position[1]
      tempString = "Bishop [" + let + "," + num + "]: "
      # get all the diagonal moves for bishop
      arr = diagMove(board, let, num, player, -1)
      arr.sort()
      tempString += " ".join(arr)
      resultString += tempString + "\n"      
   return resultString.strip()

'''
Summary:
Loop through the queen array in player class and find the possible moves.

Input:
board: Two dimensional map holding all the pieces positions
player: Player who holds the pieces

Output:
resultString: Returns the string with all possible positons
'''
def queenMoves(board, player):
   resultString = ""
   # find the queen piece location
   for i in range(len(player.queen)):
      position = player.queen[i]
      let = position[0]
      num = position[1]
      tempString = "Queen [" + let + "," + num + "]: "
      # get all the possible moves for queen
      arr = horVertMove(board, let, num, player, -1) + diagMove(board, let, num, player, -1)
      arr.sort()
      tempString += " ".join(arr)
      resultString += tempString + "\n"      
   return resultString.strip()

'''
Summary:
Loop through the king array in player class and find the possible moves.

Input:
board: Two dimensional map holding all the pieces positions
player: Player who holds the pieces

Output:
resultString: Returns the string with all possible positons
'''
def kingMoves(board, player):
   resultString = ""
    # find the king pieces location
   for i in range(len(player.king)):
      position = player.king[i]
      let = position[0]
      num = position[1]
      tempString = "King [" + let + "," + num + "]: "
      # get all the possible moves for king
      arr = horVertMove(board, let, num, player, 1) + diagMove(board, let, num, player, 1)
      arr.sort()
      tempString += " ".join(arr)
      resultString += tempString + "\n"      
   return resultString.strip()

'''
Summary:
Loop through the pawn array in player class and find the possible moves. 
The pawn has special checks such as did it move before. Assume that white pawn pieces have to move up
and black pieces have to move down.

If the white pawn position is in number 2, we will assume that piece never moved before 
   and can move up two steps as well. 
If the black pawn position is in number 7, we will assume that piece never moved before
   and can move down two steps as well.

In addition we need to do side checks to verify can the pawn move diagonally

Input:
board: Two dimensional map holding all the pieces positions
player: Player who holds the pieces

Output:
resultString: Returns the string with all possible positons
'''
def pawnMoves(board, player):
   resultString = ""
   tempArray = []
   # Determine which position for pawn to move
   # White pieces move up
   offSetFront = []
   offSetSideArr = []
   if(player.name == 'w'):
      offSetFront = (1, 0)
      offSetSideArr = [(1, -1), (1, 1)]
   # black pieces move down   
   else:
      offSetFront = (-1, 0)
      offSetSideArr = [(-1, -1), (-1, 1)]

   # find the pawn pieces location
   for i in range(len(player.pawn)):
      tempArray = []
      position = player.pawn[i]
      let = position[0]
      num = position[1]
      tempString = "Pawn [" + let + "," + num + "]: "

      # Check if the piece move or not
      if((player.name == 'w' and num == "2") or (player.name == 'b' and num == "7")):
         # Did not move yet, can move two spaces
         tempArray += offSetPawn(board, let, num, player, offSetFront[0], offSetFront[1], 2, "front")
      else:       
         # Get ONE block in front of the pawn
         tempArray += offSetPawn(board, let, num, player, offSetFront[0], offSetFront[1], 1, "front")

      # Check diagonal
      for i in range(len(offSetSideArr)):
         offSetNum = offSetSideArr[i][0]
         offSetLet = offSetSideArr[i][1]
         tempArray += offSetPawn(board, let, num, player, offSetNum, offSetLet, 1, "side")

      tempArray.sort()
      tempString += " ".join(tempArray)
      resultString += tempString + "\n"
   
   return resultString.strip()
