# Daniel Ryaboshapka
# March 9th 2019 
# chess_board.py
# 
# Representation of the chess board with piece information utilizing objects. 

# BOARD REPRESENTATIONS
BOARD = [['R2','N2','B2','Q2','K2','B2','N2','R2'],
		 ['P2','P2','P2','P2','P2','P2','P2','P2'],
		 ['0','0','0','0','0','0','0','0'],
		 ['0','0','0','0','0','0','0','0'],
		 ['0','0','0','0','0','0','0','0'],
		 ['0','0','0','0','0','0','0','0'],
		 ['P1','P1','P1','P1','P1','P1','P1','P1',],
		 ['R1','N1','B1','Q1','K1','B1','N1','R1']]

READ_IN_BOARD = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
				 ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
				 ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
				 ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
				 ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
				 ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
				 ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
				 ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']] ## CONSTANT REPRESENTATION

GAME_BOARD = [['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0'],
			  ['0','0','0','0','0','0','0','0']]

# CONSTANTS 
WHITE = 1
BLACK = 2
EMPTY_SQUARE = '0'

# MOVESETS 
KING = 'king'
QUEEN = 'queen'
ROOK = 'rook'
BISHOP = 'bishop'
KNIGHT = 'knight'
PAWN = 'pawn'

#KEYWORDS 
OFFBOARD = 'off-board'

def read_in_board():
	y = 0
	x = 0
	for column in BOARD:
		x = 0
		for row_item in column: 
			chess_piece = ' '
			populated = False
			# print(f"x,y: {x},{y}")
			if 'P' in row_item:
				populate = True
				if '2' in row_item:
					chess_piece = Pawn(BLACK, READ_IN_BOARD[y][x])
				else:
					chess_piece = Pawn(WHITE, READ_IN_BOARD[y][x])

			elif 'R' in row_item:
				populate = True
				if '2' in row_item:
					chess_piece = Rook(BLACK, READ_IN_BOARD[y][x])
				else:
					chess_piece = Rook(WHITE, READ_IN_BOARD[y][x])

			elif 'N' in row_item:
				populate = True
				if '2' in row_item:
					chess_piece = Knight(BLACK, READ_IN_BOARD[y][x])
				else:
					chess_piece = Knight(WHITE, READ_IN_BOARD[y][x])

			elif 'B' in row_item:
				populate = True
				if '2' in row_item:
					chess_piece = Bishop(BLACK, READ_IN_BOARD[y][x])
				else:
					chess_piece = Bishop(WHITE, READ_IN_BOARD[y][x])

			elif 'Q' in row_item:
				populate = True
				if '2' in row_item:
					chess_piece = Queen(BLACK, READ_IN_BOARD[y][x])
				else:
					chess_piece = Queen(WHITE, READ_IN_BOARD[y][x])

			elif 'K' in row_item:
				populate = True
				if '2' in row_item:
					chess_piece = King(BLACK, READ_IN_BOARD[y][x])
				else:
					chess_piece = King(WHITE, READ_IN_BOARD[y][x])

			if populate:
				GAME_BOARD[y][x] = chess_piece
			else:
				GAME_BOARD[y][x] = ' '
			x += 1
		y += 1
	return GAME_BOARD

# def updateBoard():

class ChessPiece:

	def __init__(self, color, position):
		self.color = color
		self.alive = True
		self.position = position

	def get_position(self):
		return self.position

	def is_captured(enemyPiece):
		self.alive = False
		self.position = OFFBOARD

	def capture(enemyPiece):
		self.position = enemyPiece.get_position()
		enemyPiece.is_captured()


class Pawn(ChessPiece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.moveSet = PAWN
		self.score = 1

	def __str__(self):
		return "P" + str(self.color)


class Knight(ChessPiece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.moveSet = KNIGHT
		self.score = 3

	def __str__(self):
		return "N" + str(self.color)

class Bishop(ChessPiece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.moveSet = BISHOP
		self.score = 3

	def __str__(self):
		return "B" + str(self.color)

class Rook(ChessPiece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.moveSet = ROOK
		self.score = 5

	def __str__(self):
		return "R" + str(self.color)

class Queen(ChessPiece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.moveSet = QUEEN
		self.score = 8

	def __str__(self):
		return "Q" + str(self.color)

class King(ChessPiece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.inCheck = False
		self.moveSet = KING
		self.score = 500

	def __str__(self):
		return "K" + str(self.color)


# def main():
# 	GAME_BOARD = read_in_board()
# 	for column in GAME_BOARD:
# 		for row in column:
# 			print(row, end = " ")
# 		print()


if __name__ == '__main__':
	main()


