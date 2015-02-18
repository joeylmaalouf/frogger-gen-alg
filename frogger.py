from subprocess import call
from sys import argv
from time import sleep


class Data(object):
	def __init__(self, path):
		self.done = False
		self.board = [list(r) for r in open(path).read().split("\n")[:-1]]
		self.cars = []
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				if self.board[row][col] is "%":
					self.prow = row
					self.pcol = col
				elif self.board[row][col] is "=":
					self.erow = row
					self.ecol = col
				elif self.board[row][col] is "o":
					self.cars.append([row, col])


	def update_player(self, move):
		self.board[self.prow][self.pcol] = " "

		if move is "r" and (self.pcol < len(self.board[self.prow])-2 or self.board[self.prow][self.pcol+1] is "="):
			self.pcol += 1
		elif move is "l" and self.pcol > 1:
			self.pcol -= 1
		elif move is "d" and self.prow < len(self.board)-2:
			self.prow += 1
		elif move is "u" and self.prow > 1:
			self.prow -= 1

		if self.prow == self.erow and self.pcol == self.ecol:
			self.done = True
			self.board[self.prow][self.pcol] = "+"
		else:
			self.board[self.prow][self.pcol] = "%"


	def update_cars(self):
		for car in self.cars:
			if self.board[car[0]][car[1]] is not "%":
				self.board[car[0]][car[1]] = " "
			if car[0] == len(self.board)-2:
				car[0] = 1
			else:
				car[0] += 1
			self.board[car[0]][car[1]] = "o"
			if car[0] == self.prow and car[1] == self.pcol:
				self.done = True
				self.board[car[0]][car[1]] = "x"


	def display(self):
		call("clear")
		for row in self.board:
			print("".join(row))


def main(argv):
	if len(argv) < 1:
		return
	visualize = bool(argv[0])
	inputs = argv[1:] if argv[1] in ["l", "r", "u", "d", "s"] else argv[2:]
	data = Data("level1.txt")  # Must be rectangular!
	for i in inputs:
		data.update_player(i)
		data.update_cars()
		if visualize:
			sleep(0.25)
			data.display()
		if data.done:
			break
	return data


if __name__ == "__main__":
	main(argv)
