



class MaxPQ:
	# initializes an empty MaxPQ
	def __init__(self, capacity):
		self.pq = [None] * capacity
		self.size = 0

	# is PQ empty?
	def isEmpty(self):
		return self.size == 0

	# returns size of PQ
	def size(self):
		return self.size
	
	# inserts key into PQ
	def insert(self, key):
		# resize array if necessary
		if self.size == (len(self.pq) - 1):
			self._resize(2 * len(self.pq))

		self.size += 1
		self.pq[self.size] = key
		self._swim(self.size)
		assert self._isMaxHeap()

	
	# returns the max element if not empty
	def max(self):
		if self.isEmpty():
			print("PQ is empty")
			return None
		return self.pq[1]

	# helper function to resize the array
	def _resize(self, new_capacity):
		if new_capacity <= len(self.pq):
			return
		old_capacity = len(self.pq)
		for i in range(old_capacity, new_capacity + 1):
			self.pq.append(None)

	# deletes and returns the max element in PQ
	def del_max(self):
		
		if self.isEmpty():
			print("PQ is Empty")
			return None

		max_key = self.pq[1]
		
		self._exch(1, self.size)
		self.size -= 1
		self._sink(1)
		self.pq[self.size + 1] = None
		assert self._isMaxHeap()
		return max_key


	# Helper functions to restore the heap invariant.

	def _swim(self, k):
		while k > 1 and self._less(k//2, k):
			self._exch(k, k//2)
			k = k//2

	def _sink(self, k):
		while 2*k <= self.size: 
			j = 2*k;
			if j < self.size and self._less(j, j+1):
				j += 1
			if not self._less(k, j):
				break
			self._exch(k, j);
			k = j;

		
	# Helper functions for compares and swaps
	def _less(self, i, j):
		return self.pq[i] < self.pq[j];
	

	def  _exch(self, i, j):
		swap = self.pq[i];
		self.pq[i] = self.pq[j];
		self.pq[j] = swap;

	# is subtree of pq[1..n] rooted at k a max heap?
	def _isMaxHeap(self, k = 1):
		if k > self.size:
			return True
		left_child = 2 * k
		right_child = 2*k + 1
		# check if the children satisfy the heap property
		if (left_child <= self.size and self._less(k, left_child)):
			return False
		if (right_child <= self.size and self._less(k, right_child)):
			return False
		# then check if both children's subtress satisfy the heap property
		return self._isMaxHeap(left_child) and self._isMaxHeap(right_child)
		


pq = MaxPQ(10)
pq.insert("this")
pq.insert("is")
pq.insert("a")
pq.insert("test")
while not pq.isEmpty():
	print(pq.del_max()) # this test is a
