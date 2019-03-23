# Daniel Ryaboshapka
# March 23
# 
# directional_output.py
# Returns diagonal, horizontal, L, or vertical representations of an 8x8 matrix 
# given a position

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
