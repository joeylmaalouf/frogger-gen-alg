from sys import argv
from time import sleep

import frogger


def main(argv):
	with open("solution.txt", "r") as solfile:
		moves = list(solfile.read()[:-1])
		print(moves)
		sleep(1)
		frogger.main([1]+moves)


if __name__ == "__main__":
	main(argv)
