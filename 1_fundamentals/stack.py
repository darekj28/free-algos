
# helper linked list class
class Node:
	def __init__(self, item):
		self.item = item
		self.next = None


class Stack:

	# creates an empty Stack
	def __init__(self):
		self._n = 0
		self._first = None

	# adds an item to the stack
	def push(self, item):
		old_first = self._first
		self._first = Node(item)
		self._first.next = old_first
		self._n += 1

	# removes and returns the most recently added item 
	def pop(self):
		assert (self.isEmpty() == False)
		item = self._first.item
		self._first = self._first.next
		self._n -= 1
		return item

	# Returns a boolean indicating if the stack is empty
	def isEmpty(self):
		return self.size() == 0

	# returns the number of items in the stack
	def size(self):
		return self._n

	# returns a list of items in the stack.
	def items(self):
		output = []
		x = self._first
		while x is not None:
			output.append(x.item)
			x = x.next
		return output




if __name__ == "__main__":
	stack = Stack()
	for i in range(0, 5)[::-1]:
		stack.push(i)

	for item in stack.items():
		print(item)
	# prints : 0,1,2,3,4

	while stack.isEmpty() == False:
		print(stack.pop(), stack.size())  

	# prints 
	# (0, 4)
	# (1, 3)
	# (2, 2)
	# (3, 1)
	# (4, 0)