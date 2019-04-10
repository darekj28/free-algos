import random
from stopwatch import Stopwatch
from three_sum import ThreeSum

MAXIMUM_INTEGER = 100000

class DoublingTest:

	# returns the time it takes to call ThreeSum.count() 
	# for random list of integers
	@staticmethod
	def time_trial(n):
		a =[]
		for i in range(0, n):
			a.append(random.randint(-MAXIMUM_INTEGER, MAXIMUM_INTEGER))

		stopwatch = Stopwatch()
		ThreeSum.count(a)
		return stopwatch.elapsed_time()


if __name__ == "__main__":
	sample_input_sizes = [2 ** i for i in range(0, 10)]
	# prints the time it takes to compute ThreeSum for random inputs of each size
	run_times = []
	for input_size in sample_input_sizes:
		run_times.append(DoublingTest.time_trial(input_size))

	for i in range(0, len(sample_input_sizes)):
		print("%d took %f seconds" % (sample_input_sizes[i], run_times[i]))

	print()
	# prints the ratio between each input size
	for i in range(0, len(sample_input_sizes) - 1):
		print("%d took %f times as long as %d" %
		 (sample_input_sizes[i + 1], run_times[i+1] / run_times[i], sample_input_sizes[i]))


