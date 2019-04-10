import stddraw

class Point:

	# x,y must be integer values
	def __init__(self, x, y):
		self._x = int(x)
		self._y = int(y)

	# returns the x-coordinate
	def x(self):
		return self._x

	# returns the y-coordinate
	def y(self):
		return self._y

	# returns a string representation of this point
	def __str__(self):
		return "(" + str(self._x) + ", " + str(self._y) + ")"

	# is this point less than that point?
	# sort by y coordinate first then use x-coordinate to break ties.
	def __lt__(self, that_point):

	# returns the slope between this point and that point
	def slopeTo(self, that_point):

	# draw this point 
	def draw(self):
		#DO NOT MODIFY
		stddraw.point(self.x(), self.y())

	# draw a line connecting this point to that point
	def drawTo(self, that_point):
		#DO NOT MODIFY
		stddraw.line(self.x(), self.y(), that_point.x(), that_point.y());

