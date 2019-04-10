# You will want to use the following Node class to write your BST
class Node:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

class BST:
	# initializes an empty BST
	def __init__(self):

	# inserts the given value into the BST
	# put duplicate values in the left subtree
	def put(self, value):

	# Return true if BST contains the value
	# returns false otherwise
	def contains(self, value):

	# deletes the given value from the BST if it exists, 
	# returns that value if it exists. Returns null if the value does not exist
	def delete(self, value):

	# returns the size of this BST
	def size(self):

	# returns true if the BST is empty, false otherwise
	def is_empty(self):

	# returns an iterator for all values in this BST in order
	def iterator(self):