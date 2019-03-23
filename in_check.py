# Daniel Ryaboshapka
# March 23 2019
# 
# in_check.py
# Utilizes piece_rules to determine whether the king is in check
# Checks to see if each enemy piece has an open lane to reach the king
# (or is a knight and is in a square that can attack the king)
#
# IN THE FUTURE: need to figure out how to condense and optimize this algorithm

from piece_rules import *
from directional_output import *
from chess_board import *
from player import *

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