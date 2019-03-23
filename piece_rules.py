# Daniel Ryaboshapka
# March 23 2019
#
# piece_rules.py
# Returns valid moves of chess pieces given the state of the game board 

from chess_board import *
from directional_output import *
from chess_game import *
import copy

EMPTY_BOARD =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def getYRepresentation(GAME_BOARD):

	Y_BOARD = copy.deepcopy(EMPTY_BOARD)

	for x in range(0,8):
		for y in range(0,8):
		 	Y_BOARD[x][y] = GAME_BOARD[y][x]

	return Y_BOARD


def pawnRules(valid_input, player, player2, GAME_BOARD):
	side = player.getColor()
	piece = valid_input[3]
	enemy = checkNearestEnemy(piece, side, GAME_BOARD)
	position = piece.get_position()
	rip_position = list(position)
	letter = rip_position[0]
	number = int(rip_position[1])
	true_position = piece.get_true_position()

	valid_moves = []

	if side == "WHITE":
		left_diagonal = (true_position[0] - 1, true_position[1] - 1)
		right_diagonal = (true_position[0] - 1, true_position[1] + 1)
		# print(f"{left_diagonal} {right_diagonal}")
		if left_diagonal[0] < 0 or left_diagonal[1] < 0:
			left_diagonal = "x"
		if right_diagonal[0] < 0 or right_diagonal[1] > 7:
			right_diagonal = "x"

		vertical = (true_position[0] - 1, true_position[1])
		if vertical[0] < 0:
			vertical = "x"
		if not isinstance(vertical, str):
			if isinstance(GAME_BOARD[vertical[0]][vertical[1]], str):
				if number == 2:
					valid_moves.append((letter + str(number + 1)))
					valid_moves.append((letter + str(number + 2)))
				else:
					valid_moves.append((letter + str(number + 1)))

		if not isinstance(left_diagonal, str):
			if "2" in str(enemy[left_diagonal[0]][left_diagonal[1]]):
				valid_moves.append(READ_IN_BOARD[left_diagonal[0]][left_diagonal[1]])
		if not isinstance(right_diagonal, str):
			if "2" in str(enemy[right_diagonal[0]][right_diagonal[1]]):
				valid_moves.append(READ_IN_BOARD[right_diagonal[0]][right_diagonal[1]])
	else:
		left_diagonal = (true_position[0] + 1, true_position[1] - 1)
		right_diagonal = (true_position[0] + 1, true_position[1] + 1)
		# print(f"{left_diagonal} {right_diagonal}")
		if left_diagonal[0] > 7 or left_diagonal[1] < 0:
			left_diagonal = "x"
		if right_diagonal[0] > 7 or right_diagonal[1] > 7:
			right_diagonal = "x"

		vertical = (true_position[0] + 1, true_position[1])
		if vertical[0] > 7:
			vertical = "x"
		if not isinstance(vertical, str):
			if isinstance(GAME_BOARD[vertical[0]][vertical[1]], str):
				if number == 7:
					valid_moves.append((letter + str(number - 1)))
					valid_moves.append((letter + str(number - 2)))
				else:
					valid_moves.append((letter + str(number - 1)))

		if not isinstance(left_diagonal, str):
			if "1" in str(enemy[left_diagonal[0]][left_diagonal[1]]):
				valid_moves.append(READ_IN_BOARD[left_diagonal[0]][left_diagonal[1]])
		if not isinstance(right_diagonal, str):
			if "1" in str(enemy[right_diagonal[0]][right_diagonal[1]]):
				valid_moves.append(READ_IN_BOARD[right_diagonal[0]][right_diagonal[1]])

	if not valid_moves:
		print("No valid moves. Pick another piece.")
		return False
	else:
		print(f"Valid moves are {valid_moves}\n")
		check = finalize(valid_moves, GAME_BOARD, piece, player, player2)
		if check:
			return True
		else:
				return False

def checkBishop(side, true_position, GAME_BOARD):
	valid_moves = []

	diagonal = diagonals(true_position)

	dia_list = getQuadrants(diagonal, true_position)

	right_up = dia_list[0]
	right_down = dia_list[1]
	left_up = dia_list[2]
	left_down = dia_list[3]

	#first split diagonals into 4 

	if side == "WHITE":  
		if len(right_up) != 0:
			for pos in right_up:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
		if len(right_down) != 0:
			for pos in right_down:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
		if len(left_up) != 0:
			for pos in left_up:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break			
		if len(left_down) != 0:
			for pos in left_down:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break

	else: 
		if len(right_up) != 0:
			for pos in right_up:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
		if len(right_down) != 0:
			for pos in right_down:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
		if len(left_up) != 0:
			for pos in left_up:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break			
		if len(left_down) != 0:
			for pos in left_down:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
	return valid_moves


def checkRook(side, true_position, GAME_BOARD):
	valid_moves = []

	regular = regulars(true_position)

	splits = splitRegulars(regular, true_position)

	left = splits[0]
	right = splits[1]
	up = splits[2]
	down = splits[3]

	if side == "WHITE":
		if len(left) != 0:
			for pos in left:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
		if len(right) != 0:
			for pos in right:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break

		if len(up) != 0:
			for pos in up:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break

		if len(down) != 0:
			for pos in down:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
	else:
		if len(left) != 0:
			for pos in left:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break

		if len(right) != 0:
			for pos in right:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break

		if len(up) != 0:
			for pos in up:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break

		if len(down) != 0:
			for pos in down:
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				else:
					if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
						valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
					break
	return valid_moves

def bishopRules(valid_input, player, player2, GAME_BOARD):
	side = player.getColor()
	piece = valid_input[3]
	enemy = checkNearestEnemy(piece, side, GAME_BOARD)
	true_position = piece.get_true_position()

	valid_moves = checkBishop(side, true_position, GAME_BOARD)

	if not valid_moves:			
		print("No valid moves. Pick another piece.")
		return False
	else:
		print(f"Valid moves are {valid_moves}\n")
		check = finalize(valid_moves, GAME_BOARD, piece, player, player2)
		if check:
			return True
		else:
			return False	

def rookRules(valid_input, player, player2, GAME_BOARD):
	side = player.getColor()
	piece = valid_input[3]
	enemy = checkNearestEnemy(piece, side, GAME_BOARD)
	true_position = piece.get_true_position()

	valid_moves = checkRook(side, true_position, GAME_BOARD)

	if not valid_moves:			
		print("No valid moves. Pick another piece.")
		return False
	else:
		print(f"Valid moves are {valid_moves}\n")
		check = finalize(valid_moves, GAME_BOARD, piece, player, player2)
		if check:
			return True
		else:
			return False	

def queenRules(valid_input, player, player2, GAME_BOARD):
	side = player.getColor()
	piece = valid_input[3]
	enemy = checkNearestEnemy(piece, side, GAME_BOARD)
	true_position = piece.get_true_position()

	valid_moves1 = checkRook(side, true_position, GAME_BOARD)
	valid_moves2 = checkBishop(side, true_position, GAME_BOARD)
	flatten = (valid_moves1, valid_moves2)

	valid_moves = []

	if not flatten:			
		print("No valid moves. Pick another piece.")
		return False
	else:
		for sub in flatten:
			for item in sub:
				valid_moves.append(item)

		print(f"Valid moves are {valid_moves}\n")
		check = finalize(valid_moves, GAME_BOARD, piece, player, player2)
		if check:
			return True
		else:
			return False	

def knightRules(valid_input, player, player2, GAME_BOARD):
	side = player.getColor()
	piece = valid_input[3]
	true_position = piece.get_true_position()

	valid_moves = []

	L = getLs(true_position)

	if side == "WHITE":
		for pos in L:
			if pos != 'x':
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				elif "2" in str(GAME_BOARD[pos[0]][pos[1]]): 
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
	else:
		for pos in L:
			if pos != 'x':
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				elif "1" in str(GAME_BOARD[pos[0]][pos[1]]): 
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])

	if not valid_moves:			
		print("No valid moves. Pick another piece.")
		return False
	else:
		print(f"Valid moves are {valid_moves}\n")
		check = finalize(valid_moves, GAME_BOARD, piece, player, player2)
		if check:
			return True
		else:
			return False			

def kingRules(valid_input, player, player2, GAME_BOARD):
	side = player.getColor()
	piece = valid_input[3]
	true_position = piece.get_true_position()

	valid_moves = []

	total = getAllAround(true_position)

	if side == "WHITE":
		for pos in total:
			if pos != 'x':
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				elif "2" in str(GAME_BOARD[pos[0]][pos[1]]): 
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
	else:
		for pos in total:
			if pos != 'x':
				if isinstance(GAME_BOARD[pos[0]][pos[1]], str):
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])
				elif "1" in str(GAME_BOARD[pos[0]][pos[1]]): 
					valid_moves.append(READ_IN_BOARD[pos[0]][pos[1]])

	if not valid_moves:			
		print("No valid moves. Pick another piece.")
		return False
	else:
		print(f"Valid moves are {valid_moves}\n")
		check = finalize(valid_moves, GAME_BOARD, piece, player, player2)
		if check:
			return True
		else:
			return False



def finalize(valid_moves, GAME_BOARD, piece, player, player2):
	new_position = "x"
	test = False
	while test == False:
		new_input = False
		while isinstance(new_input, bool):
			new_input = getNewPosition()
		new_position = new_input[1] + new_input[2]
		if new_position not in valid_moves:
			test = False
		else:
			test = True

	check = updateBoard(new_position, piece, player, player2, GAME_BOARD)
	if check:
		return True
	else:
		return False

def checkNearestEnemy(piece, side, GAME_BOARD):
	enemies = copy.deepcopy(EMPTY_BOARD)
	position = piece.get_position()
	tp = piece.get_true_position()

	Y_BOARD = getYRepresentation(GAME_BOARD)

	x_list = GAME_BOARD[tp[0]]
	y_list = Y_BOARD[tp[1]]

	enemies[tp[0]] = x_list
	for x in range(0,8):
		enemies[x][tp[1]] = y_list[x]

	diagonal = diagonals(tp)
	left = diagonal[0]
	right = diagonal[1]
	for l in left:
		enemies[l[0]][l[1]] = GAME_BOARD[l[0]][l[1]]
	for r in right:
		enemies[r[0]][r[1]] = GAME_BOARD[r[0]][r[1]]

	# if side == "WHITE":
	# 	for x in range(0,8):
	# 		for y in range(0,8):
	# 			if "1" in str(enemies[x][y]):
	# 				enemies[x][y] = "  "

	# else:
	# 	for x in range(0,8):
	# 		for y in range(0,8):
	# 			if "2" in str(enemies[x][y]):
	# 				enemies[x][y] = "  "

	# printGameBoard(enemies)

	return enemies
