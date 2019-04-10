
# helper linked list class
class Node:
	def __init__(self, item):
		self.item = item
		self.next = None


class Queue:
	# creates an empty Queue
	def __init__(self):
		self._n = 0
		self._first = None
		self._last = None

	# adds an item to the queue
	def enqueue(self, item):
		old_last = self._last
		self._last = Node(item)
		self._last.next = None
		if self.isEmpty():
			self._first = self._last
		else:
			old_last.next = self._last
		self._n += 1


	# removes and returns the least recently added item 
	def dequeue(self):
		assert self.isEmpty() == False
		item = self._first.item
		self._first = self._first.next
		self._n -= 1
		if self.isEmpty():
			self._last = None
		return item

	# Returns a boolean indicating if the queue is empty
	def isEmpty(self):
		return self.size() == 0

	# returns the number of items in the queue
	def size(self):
		return self._n

	# returns a list of items in the queue
	def items(self):
		output = []
		x = self._first
		while x is not None:
			output.append(x.item)
			x = x.next
		return output




if __name__ == "__main__":
	queue = Queue()
	for i in range(0, 5):
		queue.enqueue(i)

	for item in queue.items():
		print(item)
	# prints : 0,1,2,3,4

	while queue.isEmpty() == False:
		print(queue.dequeue(), queue.size())  
	# (0, 4)
	# (1, 3)
	# (2, 2)
	# (3, 1)
	# (4, 0)
