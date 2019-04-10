# Use this Node class to implement stack
class Node:
	def __init__(self, val = None):
		self.val = val
		self.next = None


class Stack:
	# Initializes an empty stack
	def __init__(self):
		pass

	# returns True if the stack is empty 
	# and False otherwise
	def isEmpty(self):
		pass

	# returns the number of elements in the stack
	def size(self):
		pass

	# pushes a value onto the stack
	# return value: void
	def push(self, value):
		pass

	# pops the top value off of the stack
	# and returns that item. 
	# If the stack is empty simply return None and do nothing
	def pop(self):
		pass

	# returns the item at the top of the stack
	# but does not modify the stack
	def peek(self):
		pass

