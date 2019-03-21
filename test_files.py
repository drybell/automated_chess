def pawnRules(position, player):
	side = player.getColor()
	valid_pawns = []
	pawn_positions = []
	pawn_letters = []

	if side is "WHITE":
		valid_pawns = getPieces('P1')
	else:
		valid_pawns = getPieces('P2')

	for pawn in valid_pawns:
		number_index = pawn.get_position()
		number_index = list(number_index)
		number = number_index[1]
		pawn_letters.append(number_index[0])
		pawn_positions.append(number)

	sub_pos = list(position)
	y_position = int(sub_pos[1])
	x_position = sub_pos[0]

	for curr_pos in valid_pawns:
		if side is "WHITE":
			if curr_pos in READ_IN_BOARD[6]:
				if y_position <= 2 and y_position > 4:
					print("Invalid move")
					return [False, None]
			else:
				test_true = False
				count = 0
				current_piece = " "
				for y in pawn_positions:
					if y_position != (y + 1):
						test_true = False
					else: 
						for x in pawn_letters:
							if x_position 
						test_true = True
						current_piece = valid_pawns[count]
						break
					count += 1
				if test_true == False:
					print("Invalid move")
					return [False, None]
				else: 
					return [True, position]
			else:
				return [False, None]

		else:
			if curr_pos in READ_IN_BOARD[1]:
				if y_position >= 7 and y_position < 5:
					print("Invalid move")
					return [False, None]
				else:
					test_true = False
					for x in pawn_positions:
						if y_position != (x - 1):
							test_true = False
						else: 
							test_true = True
							break
					if test_true == False:
						print("Invalid move")
						return [False, None]
					else: 
						return [True, position]
			else:
				return [False, None]
		return [False, None]