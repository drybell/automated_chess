# Daniel Ryaboshapka
# March 12 2019
# 
# chess_game.py
# Handles movements, utilizes chess_board library for environment

from chess_board import *
import copy

EMPTY_BOARD =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


check_array1 = ['P', 'N', 'B','R', 'Q', 'K']
check_array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
check_array3 = ['1','2','3','4','5','6','7','8']

off_board_white = []
off_board_black = []


class Player():
	def __init__(self, color):
		self.color = color
		self.score = []
		self.alive = True
		self.currentTurn = False

	def getColor(self):
		return self.color

	def setTurn(self, isTrue):
		if isTrue == False:
			self.currentTurn = False
		else:
			self.currentTurn = True

	def getTurn(self):
		return self.currentTurn

	def __str__(self):
		return self.color + " " + self.score

def getLs(true_position):

	x = true_position[0]
	y = true_position[1]

	#clockwise rotation at right side

	x1 = x - 2
	y1 = y + 1

	x2 = x - 1
	y2 = y + 2

	x3 = x + 1
	y3 = y + 2

	x4 = x + 2
	y4 = y + 1

	x5 = x + 2
	y5 = y - 1

	x6 = x + 1
	y6 = y - 2

	x7 = x - 1
	y7 = y - 2

	x8 = x - 2
	y8 = y - 1

	L = [(x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5), (x6,y6), (x7,y7), (x8,y8)]
	for x in range(0,8):
		item = L[x]
		if (item[0] < 0 or item[0] > 7):
			L[x] = 'x'
		elif (item[1] < 0 or item[1] > 7):
			L[x] = 'x'
	return L

def diagonals(true_position):
	left_diagonal = []
	right_diagonal = []

	x_pos = true_position[0]
	y_pos = true_position[1]

	x_pos2 = true_position[0]
	y_pos2 = true_position[1]

	x_pos3 = true_position[0]
	y_pos3 = true_position[1]

	x_pos4 = true_position[0]
	y_pos4 = true_position[1]

	for x in range(0,8):
		x_pos -= 1
		y_pos += 1
		if x_pos < 0 or x_pos > 7:
			break
		if y_pos < 0 or y_pos > 7: 
			break
		left_diagonal.append((x_pos,y_pos))

	# print(f"{x_pos} {y_pos} {x_pos2} {y_pos2} {x_pos3} {y_pos3} {x_pos4} {y_pos4}")

	for x in range(0,8):
		x_pos2 += 1
		y_pos2 -= 1
		if x_pos2 < 0 or x_pos2 > 7:
			break
		if y_pos2 < 0 or y_pos2 > 7: 
			break
		left_diagonal.append((x_pos2,y_pos2))

	# print(f"{x_pos} {y_pos} {x_pos2} {y_pos2} {x_pos3} {y_pos3} {x_pos4} {y_pos4}")

	for x in range(0,8):
		x_pos3 += 1
		y_pos3 += 1
		if x_pos3 < 0 or x_pos3 > 7:
			break
		if y_pos3 < 0 or y_pos3 > 7: 
			break
		right_diagonal.append((x_pos3,y_pos3))

	# print(f"{x_pos} {y_pos} {x_pos2} {y_pos2} {x_pos3} {y_pos3} {x_pos4} {y_pos4}")

	for x in range(0,8):
		x_pos4 -= 1
		y_pos4 -= 1
		if x_pos4 < 0 or x_pos4 > 7:
			break
		if y_pos4 < 0 or y_pos4 > 7: 
			break
		right_diagonal.append((x_pos4,y_pos4))
	# print(f"{x_pos} {y_pos} {x_pos2} {y_pos2} {x_pos3} {y_pos3} {x_pos4} {y_pos4}")

	totals = (left_diagonal, right_diagonal)
	return totals


def regulars(true_position):
	horizontal = []
	vertical = []

	x_pos = true_position[0]
	y_pos = true_position[1]

	#left first, then right
	#up first, then down

	if x_pos == 0 or y_pos == 0:
		if x_pos == 0 and y_pos == 0:
			for x in range(1, 8):
				vertical.append((x,y_pos))
			for y in range(1, 8):
				horizontal.append((x_pos,y))
		elif x_pos == 0:
			for y in range(y_pos - 1, -1, -1):
				horizontal.append((x_pos,y))
			for y in range(y_pos + 1, 8):
				horizontal.append((x_pos,y))
			for x in range(1, 8):
				vertical.append((x,y_pos))
		elif y_pos == 0:
			for x in range(x_pos - 1, -1, -1):
				vertical.append((x,y_pos))
			for x in range(x_pos + 1, 8):
				vertical.append((x,y_pos))
			for y in range(1, 8):
				horizontal.append((x_pos,y))

	elif x_pos == 7 or y_pos == 7:
		if x_pos == 7 and y_pos == 7:
			for x in range(7, -1, -1):
				vertical.append((x,y_pos))
			for y in range(7, -1, -1):
				horizontal.append((x_pos,y))
		elif x_pos == 7:
			for y in range(y_pos - 1, -1, -1):
				horizontal.append((x_pos,y))
			for y in range(y_pos + 1, 8):
				horizontal.append((x_pos,y))
			for x in range(7, -1, -1):
				vertical.append((x,y_pos))
		elif y_pos == 7:
			for x in range(x_pos - 1, -1, -1):
				vertical.append((x,y_pos))
			for x in range(x_pos + 1, 8):
				vertical.append((x,y_pos))
			for y in range(7, -1, -1):
				horizontal.append((x_pos,y))

	else:
		for y in range(y_pos - 1, -1, -1):
			horizontal.append((x_pos,y))
		for y in range(y_pos + 1, 8):
			horizontal.append((x_pos,y))

		for x in range(x_pos - 1, -1, -1):
			vertical.append((x,y_pos))
		for x in range(x_pos + 1, 8):
			vertical.append((x,y_pos))

	return (horizontal, vertical)

def getQuadrants(diagonal, true_position):
	right = diagonal[0]
	left = diagonal[1]

	right_up = []
	right_down = []
	left_up = []
	left_down = []
	for item in right:
		if item[0] < true_position[0]:
			right_up.append(item)
		else:
			right_down.append(item)

	for item in left:
		if item[0] < true_position[0]:
			left_up.append(item)
		else:
			left_down.append(item)

	return (right_up, right_down, left_up, left_down)

def splitRegulars(regular, true_position):
	horizontal = regular[0]
	vertical = regular[1]

	left = []
	right = []
	down = []
	up = []

	for item in horizontal:
		if item[1] < true_position[1]:
			left.append(item)
		else:
			right.append(item)

	for item in vertical:
		if item[0] < true_position[0]:
			up.append(item)
		else:
			down.append(item)

	return (left, right, up, down)

def getAPiece(GAME_BOARD, myPlayer):
	color = myPlayer.getColor()
	print(f"{color} Player", end = " ")
	check_input = input("Enter a position for a piece (ex. Ph2): ")
	input_list = []
	turn = myPlayer.getTurn()
	check = False

	if len(check_input) != 3:
		print("Try Again.")
		return False
	else:
		input_list = list(check_input)
		if input_list[0] not in check_array1:
			print(input_list[0])
			print("Try Again.")
			return False
		if input_list[1] not in check_array2:
			print(input_list[1])
			print("Try Again")
			return False
		if input_list[2] not in check_array3:
			print(input_list[2])
			print("Try Again")
			return False

	position = input_list[1] + input_list[2]
	name = input_list[0]

	for column in GAME_BOARD:
		for row_item in column:
			if name in str(row_item):
				# print(name)
				# print(row_item)
				# print(position)
				# print(row_item.get_position())
				if position == row_item.get_position():
					if row_item.get_color() == 1 and color == "BLACK":
						print("Wrong Side")
						check = False
						break
					elif row_item.get_color() == 2 and color == "WHITE":
						print("Wrong Side")
						check = False
						break
					else:
						input_list.append(row_item)
						check = True
						break

	if check == False:
		return False 
	else:
		return input_list


def pickAPiece(valid_input, player1, player2, GAME_BOARD):
	current_piece = valid_input[0]
	position = valid_input[1] + valid_input[2]
	actual_piece = valid_input[3]
	all_pieces = {
		'P': pawnRules,
		'N': knightRules,
		'B': bishopRules,
		'R': rookRules,
		'Q': queenRules,
		'K': kingRules
	}
	function = all_pieces.get(current_piece)
	test = function(valid_input, player1, player2, GAME_BOARD)
	if test == False:
		return False
	else:
		return True


def updateBoard(updated_position, curr_piece, player, player2, GAME_BOARD):
	target_piece = 0
	new_true_position = []
	color = player.getColor()
	# print(updated_position)
	for x in range(0,8):
		for y in range(0,8):
			if updated_position == READ_IN_BOARD[x][y]:
				# print(f"{x} {y}")
				# print(updated_position)
				new_true_position = (x,y)
			temp = GAME_BOARD[x][y]
			if isinstance(temp, str):
				pass
			else:
				position = temp.get_position()
				if position is updated_position:
					target_piece = GAME_BOARD[x][y]

	old_true_position = curr_piece.get_true_position()
	old_position = curr_piece.get_position()
	# print(old_position)
	GAME_BOARD[old_true_position[0]][old_true_position[1]] = ' '
	check = False

	if target_piece == 0:
		# this means that there is no piece in that position
		# so we don't have to worry about capturing 
		curr_piece.set_position(updated_position)
		curr_piece.set_true_position(new_true_position)
	else:
		curr_piece.capture(target_piece)
		curr_piece.set_true_position(updated_position)
		if color == "WHITE":
			off_board_white.append(target_piece)
		else:
			off_board_black.append(target_piece)

	# print(new_true_position)
	GAME_BOARD[new_true_position[0]][new_true_position[1]] = curr_piece
	check = inCheck(player, player2, GAME_BOARD)
	if check == True:
		if target_piece == 0:
			curr_piece.set_true_position(old_true_position)
			curr_piece.set_position(old_position)
			GAME_BOARD[new_true_position[0]][new_true_position[1]] = ' '
		else:
			if color == "WHITE":
				off_board_white.remove(target_piece)
			else:
				off_board_black.remove(target_piece)

			target_piece.set_position(updated_position)
			target_piece.set_true_position(updated_position)
			curr_piece.set_true_position(old_true_position)
			curr_piece.set_position(old_position)
			curr_piece.uncapture(target_piece, updated_position)
			GAME_BOARD[new_true_position[0]][new_true_position[1]] = target_piece
		return False

	else:
		printGameBoard(GAME_BOARD)
		return True



# def lookForCheck():



def getNewPosition():
	check_input = input("Enter a NEW POSITION for your piece: ")
	input_list = []

	if len(check_input) != 3:
		print("Try Again.")
		return False
	else:
		input_list = list(check_input)
		if input_list[0] not in check_array1:
			print(input_list[0])
			print("Try Again.")
			return False
		if input_list[1] not in check_array2:
			print(input_list[1])
			print("Try Again")
			return False
		if input_list[2] not in check_array3:
			print(input_list[2])
			print("Try Again")
			return False

	return input_list


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


def getAllAround(true_position):
	x = true_position[0]
	y = true_position[1]

	#clockwise from vertical
	x1 = x - 1
	y1 = y

	x2 = x - 1
	y2 = y + 1

	x3 = x
	y3 = y + 1

	x4 = x + 1
	y4 = y + 1

	x5 = x + 1
	y5 = y

	x6 = x + 1
	y6 = y - 1

	x7 = x
	y7 = y - 1

	x8 = x - 1
	y8 = y - 1

	total = [(x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5), (x6,y6), (x7,y7), (x8,y8)]
	for x in range(0,8):
		item = total[x]
		if (item[0] < 0 or item[0] > 7):
			total[x] = 'x'
		elif (item[1] < 0 or item[1] > 7):
			total[x] = 'x'
	return total




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



def makeMove(myPlayer, secondPlayer, GAME_BOARD, check):

	valid_move = False
	side = myPlayer.getColor()
	if check:
		while(not valid_move):
			while check:
				valid_input = getAPiece(GAME_BOARD, myPlayer)
				while isinstance(valid_input, bool):
					valid_input = getAPiece(GAME_BOARD, myPlayer)
				valid_move = pickAPiece(valid_input, myPlayer, secondPlayer, GAME_BOARD)
				check = inCheck(myPlayer, secondPlayer, GAME_BOARD)
				if check == True:
					print("Your king is still in check. Try again")

	else:
		while(not valid_move):
			valid_input = getAPiece(GAME_BOARD, myPlayer)
			while isinstance(valid_input, bool):
				valid_input = getAPiece(GAME_BOARD, myPlayer)
			valid_move = pickAPiece(valid_input, myPlayer, secondPlayer, GAME_BOARD)


def inCheck(curr_player, second_player, GAME_BOARD):
	curr_color = curr_player.getColor()
	enemy_color = second_player.getColor()
	enemy_piece = ' '

	if curr_color == "WHITE":
		for column in GAME_BOARD:
			for row_item in column:
				if "K1" == str(row_item):
					enemy_piece = row_item
	else:
		for column in GAME_BOARD:
			for row_item in column:
				if "K2" in str(row_item):	
					enemy_piece = row_item

	kings_position = enemy_piece.get_true_position()

	if curr_color == "WHITE":
		# pawn is checking king 
		left_diagonal = (kings_position[0] - 1, kings_position[1] - 1)
		right_diagonal = (kings_position[0] - 1, kings_position[1] + 1)
		if left_diagonal[0] < 0 or left_diagonal[1] < 0:
			left_diagonal = "x"
		if right_diagonal[0] < 0 or right_diagonal[1] > 7:
			right_diagonal = "x"
		if not isinstance(left_diagonal, str):
			if "P2" == str(GAME_BOARD[left_diagonal[0]][left_diagonal[1]]):
				enemy_piece.setCheck(True)
				return True
		if not isinstance(right_diagonal, str):
			if "P2" == str(GAME_BOARD[right_diagonal[0]][right_diagonal[1]]):
				enemy_piece.setCheck(True)
				return True
		# knight is checking king
		L = getLs(kings_position)
		for pos in L:
			if pos != 'x':
				if "N2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		# bishop is checking king
		diagonal = diagonals(kings_position)

		dia_list = getQuadrants(diagonal, kings_position)

		right_up = dia_list[0]
		right_down = dia_list[1]
		left_up = dia_list[2]
		left_down = dia_list[3]
		check = False

		if len(right_up) != 0:
			for pos in right_up:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right_down) != 0:
			for pos in right_down:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(left_up) != 0:
			for pos in left_up:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		
		if len(left_down) != 0:
			for pos in left_down:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		# rook is checking king 
		regular = regulars(kings_position)

		splits = splitRegulars(regular, kings_position)

		left = splits[0]
		right = splits[1]
		up = splits[2]
		down = splits[3]	

		if len(left) != 0:
			for pos in left:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right) != 0:
			for pos in right:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(up) != 0:
			for pos in up:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(down) != 0:
			for pos in down:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		#queen is checking king
		if len(left) != 0:
			for pos in left:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right) != 0:
			for pos in right:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(up) != 0:
			for pos in up:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(down) != 0:
			for pos in down:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		

		if len(right_up) != 0:
			for pos in right_up:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right_down) != 0:
			for pos in right_down:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(left_up) != 0:
			for pos in left_up:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		
		if len(left_down) != 0:
			for pos in left_down:
				if "1" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q2" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		#in faux check by other king 
		around = getAllAround(kings_position)

		for pos in around:
			if pos != 'x':
				if "K2" in str(GAME_BOARD[pos[0]][pos[1]]):
					return True

	else:

		left_diagonal = (kings_position[0] + 1, kings_position[1] - 1)
		right_diagonal = (kings_position[0] + 1, kings_position[1] + 1)
		if left_diagonal[0] > 7 or left_diagonal[1] < 0:
			left_diagonal = "x"
		if right_diagonal[0] > 7 or right_diagonal[1] > 7:
			right_diagonal = "x"
		if not isinstance(left_diagonal, str):
			if "P1" == str(GAME_BOARD[left_diagonal[0]][left_diagonal[1]]):
				enemy_piece.setCheck(True)
				return True
		if not isinstance(right_diagonal, str):
			if "P1" == str(GAME_BOARD[right_diagonal[0]][right_diagonal[1]]):
				enemy_piece.setCheck(True)
				return True

		L = getLs(kings_position)
		for pos in L:
			if pos != 'x':
				if "N1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		

		diagonal = diagonals(kings_position)

		dia_list = getQuadrants(diagonal, kings_position)

		right_up = dia_list[0]
		right_down = dia_list[1]
		left_up = dia_list[2]
		left_down = dia_list[3]
		check = False

		if len(right_up) != 0:
			for pos in right_up:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right_down) != 0:
			for pos in right_down:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(left_up) != 0:
			for pos in left_up:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		
		if len(left_down) != 0:
			for pos in left_down:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "B1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		regular = regulars(kings_position)

		splits = splitRegulars(regular, kings_position)

		left = splits[0]
		right = splits[1]
		up = splits[2]
		down = splits[3]	

		if len(left) != 0:
			for pos in left:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right) != 0:
			for pos in right:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(up) != 0:
			for pos in up:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(down) != 0:
			for pos in down:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "R1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		# queen check

		if len(left) != 0:
			for pos in left:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right) != 0:
			for pos in right:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(up) != 0:
			for pos in up:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		if len(down) != 0:
			for pos in down:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		

		if len(right_up) != 0:
			for pos in right_up:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(right_down) != 0:
			for pos in right_down:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True
		if len(left_up) != 0:
			for pos in left_up:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True		
		if len(left_down) != 0:
			for pos in left_down:
				if "2" in str(GAME_BOARD[pos[0]][pos[1]]):
					check = False
					break
				if "Q1" in str(GAME_BOARD[pos[0]][pos[1]]):
					enemy_piece.setCheck(True)
					return True

		around = getAllAround(kings_position)

		for pos in around:
			if pos != 'x':
				if "K1" in str(GAME_BOARD[pos[0]][pos[1]]):
					return True
	return check


def inMate(player1, player2, GAME_BOARD):
	curr_piece = ' '
	valid_input = ""
	side_of_mate = player2.getColor()
	color = 0
	test_matrix = []
	if side_of_mate == "WHITE":
		color = "1"
	else:
		color = "2"
	for column in GAME_BOARD:
		for row_item in column:
			if not isinstance(row_item, str):
				if color in str(row_item):
					curr_piece = row_item
					name = list(str(curr_piece))
					letter = name[0]
					position = curr_piece.get_position()
					valid_input = letter + position
					valid_input = list(valid_input)
					valid_input.append(curr_piece)
					test = pickAPiece(valid_input, player1, player2, GAME_BOARD)
					test_matrix.append(test)
					valid_input = ""

	flag = False
	for item in test_matrix:
		if item:
			flag = True
			break
		else:
			pass

	if flag:
		return False
	else:
		return True
	

def checkTurn(my_player1, my_player2):
	if(my_player1.getTurn()):
		return my_player1
	else:
		return my_player2


def printGameBoard(board):
		for column in board:
			for row in column:
				if isinstance(row, str):
					print(row, end="  ")
				else:
					print(row, end=" ")
			print()


def getYRepresentation(GAME_BOARD):

	Y_BOARD = copy.deepcopy(EMPTY_BOARD)

	for x in range(0,8):
		for y in range(0,8):
		 	Y_BOARD[x][y] = GAME_BOARD[y][x]

	return Y_BOARD

def flipBoard(GAME_BOARD):

	P2_SIDE = copy.deepcopy(EMPTY_BOARD)

	for x in range(0,8):
		for y in range(0,8):
			P2_SIDE[7-x][7-y] = copy.deepcopy(GAME_BOARD[x][y])

	return P2_SIDE

def gameStep(current_player, second_player, GAME_BOARD):
	game_over = False
	check = False
	while game_over == False:
		makeMove(current_player, second_player, GAME_BOARD, check)
		check = inCheck(second_player, current_player, GAME_BOARD)
		if check:
			print("KING IS IN CHECK")
			in_mate = inMate(current_player, second_player, GAME_BOARD)
			if in_mate:
				game_over = True
				print(f"{current_player} has mated {second_player}")
				break
		current_player.setTurn(False)
		second_player.setTurn(True)
		temp = current_player
		current_player = second_player
		second_player = temp
		# flip_board = flipBoard(GAME_BOARD)
		print('_______________________\n')
		# printGameBoard(flip_board)
		printGameBoard(GAME_BOARD)

def main():

	# Initialize players and set turn to white
	white_player = Player("WHITE")
	black_player = Player("BLACK")
	current_player = white_player
	second_player = black_player
	white_player.setTurn(True)

	# Initialize game board
	GAME_BOARD = read_in_board()
	printGameBoard(GAME_BOARD)

	gameStep(current_player, second_player, GAME_BOARD)


if __name__ == '__main__':
	main()