import unittest
import stddraw

from point import Point
from brute_collinear import BruteCollinearPoints

# RS_INPUT = "./rs1423.txt"
INPUT40 = "./input40.txt"
# INPUT6 = "./input6.txt"
class TestSolution(unittest.TestCase):

	def test_brute_collinear(self):
		stddraw.setXscale(0, 32768)
		stddraw.setYscale(0, 32768)
		
		with open(INPUT40, 'r') as file:
			# create array of length N to store points
			N = int(file.readline())
			points = []
			# create points from StdIn and store them in array
			for i in range(0, N):
				line = file.readline()
				if (len(line.split(' ')) == 2):
					x = line.split(' ')[0]
					y = line.split(' ')[1]
					p = Point(x, y)
					points.append(p)

			# draw every point
			for p in points:
				p.draw()
			
			fast_collinear = BruteCollinearPoints(points)
			# print out and draw collinear points
			segments = fast_collinear.segments()
			for ps in segments:
				for i in range(0, len(ps) - 1):
					ps[i].drawTo(ps[i+1])
		stddraw.show()
		
		self.assertTrue(True)


	

if __name__ == '__main__':
	unittest.main()
