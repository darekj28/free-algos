

from stopwatch import Stopwatch

class TwoSum:
	@staticmethod 
	def get_all_solutions(a):
		solutions = []
		n = len(a)
		for i in range(0, n):
			for j in range(i + 1, n):
					if a[i] + a[j]  == 0:
						solutions.append((a[i], a[j]))

		return solutions

	@staticmethod
	def print_all(a):
		solutions = TwoSum.get_all_solutions(a)
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
	TwoSum.get_all_solutions(sample_input)
	print(stopwatch.elapsed_time())

