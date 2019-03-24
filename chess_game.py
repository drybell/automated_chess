# Daniel Ryaboshapka
# March 12 2019
# 
# chess_game.py
# Handles movements, utilizes chess_board library for environment


### TO DO: en passant, promoting pawns, draw, insufficent material, scores.

from chess_board import *
from player import *
from directional_output import *
from piece_rules import *
from in_check import *
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
	valid_moves = function(actual_piece, player1, player2, GAME_BOARD)
	if isinstance(valid_moves, bool):
		return False
	check = finalize(valid_moves, GAME_BOARD, actual_piece, player1, player2)
	return check


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


def inMate(player1, player2, GAME_BOARD):
	curr_piece = ' '
	valid_input = ""
	side_of_mate = player2.getColor()
	color = 0
	test_matrix = []
	TEST_BOARD = copy.deepcopy(GAME_BOARD)
	if side_of_mate == "WHITE":
		color = "1"
	else:
		color = "2"
	for column in GAME_BOARD:
		for row_item in column:
			if not isinstance(row_item, str):
				if color in str(row_item):
					curr_piece = row_item
					test = testRun(player1, player2, curr_piece, TEST_BOARD)
					test_matrix.append(test)
					valid_input = ""

	for item in test_matrix:
		if item == False:
			return False
	return True
			

def testRun(player1, player2, piece, TEST_BOARD):
	name = list(str(piece))
	total_checks = []
	letter = name[0]
	all_pieces = {
		'P': pawnRules,
		'N': knightRules,
		'B': bishopRules,
		'R': rookRules,
		'Q': queenRules,
		'K': kingRules
	}
	function = all_pieces.get(letter)
	valid_moves = function(piece, player1, player2, TEST_BOARD)
	if not isinstance(valid_moves, bool):
		for move in valid_moves:
			new_position = move
			check = updateTestBoard(new_position, piece, player1, player2, TEST_BOARD)
			total_checks.append(check)
	return total_checks

def updateTestBoard(updated_position, curr_piece, player, player2, TEST_BOARD):
	target_piece = 0
	new_true_position = []
	color = player.getColor()
	for x in range(0,8):
		for y in range(0,8):
			if updated_position == READ_IN_BOARD[x][y]:
				# print(updated_position)
				new_true_position = (x,y)
			temp = TEST_BOARD[x][y]
			if isinstance(temp, str):
				pass
			else:
				position = temp.get_position()
				if position is updated_position:
					target_piece = TEST_BOARD[x][y]

	old_true_position = curr_piece.get_true_position()
	old_position = curr_piece.get_position()
	# print(old_position)
	TEST_BOARD[old_true_position[0]][old_true_position[1]] = ' '

	TEST_BOARD[new_true_position[0]][new_true_position[1]] = curr_piece
	check = inCheck(player, player2, TEST_BOARD)

	TEST_BOARD[old_true_position[0]][old_true_position[1]] = curr_piece
	if not isinstance(target_piece, int):
		TEST_BOARD[new_true_position[0]][new_true_position[1]] = target_piece
	else:
		TEST_BOARD[new_true_position[0]][new_true_position[1]] = ' '	
	return check



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