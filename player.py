# This file is to create the player class to hold all the pieces

class Player(object):
   king = []
   rook = []
   bishop = []
   queen = []
   knight = []
   pawn = []
   name = ""

   def __init__(self, name, pawn, rook, knight, bishop, queen, king):
      self.king = king
      self.rook = rook
      self.bishop = bishop
      self.queen = queen
      self.knight = knight
      self.pawn = pawn
      self.name = name
