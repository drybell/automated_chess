# Daniel Ryaboshapka
# March 23 2019
#
# player.py
# Holds the player class for chess

class Player():
	def __init__(self, color):
		self.color = color
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
		return self.color