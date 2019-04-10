

from binary_search import BinarySearch
from stopwatch import Stopwatch

class ThreeSumFast:
	@staticmethod 
	def get_all_solutions(a):
		solutions = []
		sorted_a = sorted(a)
		n = len(a)
		for i in range(0, n):
			for j in range(i + 1, n):
				k = BinarySearch.binary_search(sorted_a, -(a[i] + a[j]))
				if k > j:
					solutions.append((a[i], a[j], a[k]))

		return solutions

	@staticmethod
	def print_all(a):
		solutions = ThreeSumFast.get_all_solutions(a)
		for solution in solutions:
			print(solution)

	@staticmethod
	def count(a):
		solutions = ThreeSumFast.get_all_solutions(a)
		return len(solutions)



if __name__ == "__main__":
	MIN_INPUT = -100
	MAX_INPUT = 100
	sample_input = [i for i in range(MIN_INPUT, MAX_INPUT)]
	stopwatch = Stopwatch()
	solutions = ThreeSumFast.get_all_solutions(sample_input)
	for solution in solutions:
		print(solution)
	print(stopwatch.elapsed_time())

