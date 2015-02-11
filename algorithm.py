from math import sqrt
from random import randint
from sys import argv
from time import clock

import frogger


class Individual(object):
	def __init__(self):
		self.numchros = 128
		self.dirs = ["l", "r", "u", "d", "s"]
		self.moves = [self.dirs[randint(0, 4)] for i in range(self.numchros)]
		self.fitness = 0

	def mutate(self):
		self.moves[randint(0, self.numchros-1)] = self.dirs[randint(0, 4)]

	def scramble(self):
		for i in range(self.numchros):
			self.mutate()

	def payoff(self):
		data = frogger.main([0]+self.moves)
		self.fitness = sqrt(float(data.erow-data.prow)**2 + float(data.ecol-data.pcol)**2)


def main(argv):
	sampledata = frogger.main([0]+["s"])
	distance = len(sampledata.board[0])
	popsize = 1000
	time_start = clock()
	population = [Individual() for i in range(popsize)]
	generation = 0
	while(True):
		for individual in population:
			individual.payoff()
		population.sort(key = lambda x: x.fitness)
		print("Generation {0:04d}, best solution: {1:07.4f} units away. Time taken: {2:09.4f} seconds."\
			.format(generation, population[0].fitness, clock()-time_start))

		if (population[0].fitness == 0.0):
			print("Moves:\n{0}".format(" ".join(population[0].moves)))
			with open("solution.txt", "w") as outfile:
				outfile.write("".join(population[0].moves)+"\n")
			return population[0].moves

		for individual in population[popsize//4:popsize//2]:
			individual.mutate()
		for individual in population[popsize//2:]:
			individual.scramble()
		generation += 1


if __name__ == "__main__":
	main(argv)
