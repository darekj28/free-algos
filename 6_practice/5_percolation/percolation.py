from weighted_quick_union_uf import WeightedQuickFindUF

class Percolation:
	# create N-by-N grid, with all sites blocked
	def __init__(self, N):
		#initialize your grid here

		#initialize a WeightedQuickFind object here
		#there should be N*N sites and the sites have indexes from 0 to N^2
		
		
		#A hint to make all methods constant time is to union the first row together and union the last row together but still leave the sites blocked to start off with. 


	# open site (row i, column j) if it is not already
	def open(self, i, j):

	# is site (row i, column j) open?
	def isOpen(self, i , j):

	# is site (row i, column j) full?
	def isFull(self, i, j):

	# does the system percolate?
	def percolates(self):

# Use the main method for unit tests
if __name__ == "__main__":
	pass