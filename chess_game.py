# Daniel Ryaboshapka
# March 12 2019
# 
# chess_game.py
# Handles movements, utilizes chess_board library for environment

import chess_board


check_array1 = ['P', 'N', 'B' , 'R', 'Q', 'K', 'p', 'n', 'b' , 'r', 'q', 'k']
check_array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
check_array3 = [1,2,3,4,5,6,7,8]

off_board_white = []
off_board_black = []


class Player():
	def __init__(self, color):
		self.color = color
		self.score = []
		self.alive = True
		self.currentTurn = False

	def getColor():
		return self.color

	def setTurn(isTrue):
		if isTrue == False:
			self.currentTurn = False
		else:
			self.currentTurn = True

	def getTurn():
		return self.currentTurn

	def __str__(self):
		return self.color + " " + self.score

def getCorrectInput():
	check_input = input("Enter a move: ")
	input_list = []

	if check_input.len() != 3:
		print("Try Again.")
		getCorrectInput()
	else:
		input_list = list(check_input)
		if input_list[0] not in check_array1:
			print("Try Again.")
			getCorrectInput()
		if input_list[1] not in check_array2:
			print("Try Again")
			getCorrectInput()
		if input_list[2] not in check_array3:
			print("Try Again")
			getCorrectInput()

	return input_list


def pickAPiece(current_piece, position, player):
	all_pieces = {
		'P': pawnRules,
		'N': knightRules,
		'B': bishopRules,
		'R': rookRules,
		'Q': queenRules,
		'K': kingRules
	}
	function = all_pieces.get(current_piece)
	complete = function(position, player)
	if complete[0]:
		# updateBoard()  
	else{
		getCorrectInput()
	}


def getPieces(curr_piece):
	x = 0
	y = 0
	piece_list = []
	for column in GAME_BOARD:
		x = 0
		for row_item in GAME_BOARD:
			if curr_piece is str(row_item):
				piece_list.append(row_item)
			x += 1
		y += 1
	return piece_list


def pawnRules(position, player):
	side = player.getColor()
	valid_pawns = []
	pawn_positions = []

	if side is "WHITE":
		valid_pawns = getPieces('P1')
	else:
		valid_pawns = getPieces('P2')

	for pawn in valid_pawns:
		pawn_positions.append(pawn.get_position())

	sub_pos = list(position)
	y_position = int(sub_pos[1])
	x_position = sub_pos[0]

	for curr_pos in pawn_positions:
		if side is "WHITE":
			if curr_pos in READ_IN_BOARD[6]:
				if y_position < 2 and y_position > 4:
					print("Invalid move")
					return [False, None]
				else:
					if y_position

		else:
			if curr_pos in READ_IN_BOARD[1]:
				if y_position == 5:





def knightRules(position, player):

def bishopRules(position, player):

def rookRules(position, player):

def queenRules(position, player):

def kingRules(position, player):


def makeMove(myPlayer):

	valid_move = False

	while(!valid_move){
		valid_input = getCorrectInput()
		position = valid_input[1] + valid_input[2]
		pickAPiece(valid_input[0], position, myPlayer)



		




	}



def is_off_board():


def piece_collision():


def in_check():


def inMate():



def gameStep():


def checkTurn(my_player1, my_player2):
	if(my_player1.getTurn()):
		return my_player1
	else:
		return my_player2




def main():

	# Initialize players and set turn to white
	white_player = Player("WHITE")
	black_player = Player("BLACK")
	current_player = white_player
	white_player.setTurn(True)


	# Initialize game board
	GAME_BOARD = read_in_board()

	makeMove(current_player)












if __name__ == '__main__':
	main()