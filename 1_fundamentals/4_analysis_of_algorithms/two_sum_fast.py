

from binary_search import BinarySearch
from stopwatch import Stopwatch

class TwoSumFast:
	@staticmethod 
	def get_all_solutions(a):
		solutions = []
		sorted_a = sorted(a)
		n = len(a)
		for i in range(0, n):
			j = BinarySearch.binary_search(sorted_a, -a[i])
			if j > i:
				solutions.append((a[i], a[j]))

		return solutions

	@staticmethod
	def print_all(a):
		solutions = TwoSumFast.get_all_solutions(a)
		for solution in solutions:
			print(solution)

	@staticmethod
	def count(a):
		solutions = TwoSum.get_all_solutions(a)
		return len(solutions)



if __name__ == "__main__":
	MIN_INPUT = -100
	MAX_INPUT = 100
	sample_input = [i for i in range(MIN_INPUT, MAX_INPUT)]
	stopwatch = Stopwatch()
	solutions = TwoSumFast.get_all_solutions(sample_input)
	for solution in solutions:
		print(solution)
	print(stopwatch.elapsed_time())

