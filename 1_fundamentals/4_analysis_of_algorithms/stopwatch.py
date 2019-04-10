import math
import time

class Stopwatch:
	def __init__(self):
		self._start = time.time()

	def elapsed_time(self):
		# divide by 1000 to convert from milliseconds to seconds
		return (time.time() - self._start )


def factorial_run_time_function(n):
	if n == 0:
		return 1
	else:
		for i in range(0, n):
			factorial_run_time_function(i)


if __name__ == "__main__":
	# time how long it takes to compute the sum of the 
	# squareroot of all numbers from 0 to 2^16
	stopwatch_1 = Stopwatch()
	LARGE_NUMBER = 2 ** 16
	squareroot_sum = 0
	for i in range(0, LARGE_NUMBER):
		squareroot_sum += math.sqrt(i)

	# runs almost instantly! 
	print(stopwatch_1.elapsed_time(), squareroot_sum)

	stopwatch_2 = Stopwatch()
	factorial_run_time_function(20)
	print("Factorial function takes very long:", stopwatch_2.elapsed_time())

