

class IndexMinPQ:
	def __init__(self, capacity):
		self._capacity = capacity
		self._n = 0
		self._keys = [float("infinity")] * capacity
		self._pq =  [0] * (capacity + 1)
		self._qp =  [-1] * (capacity+ 1)

	def isEmpty(self):
		return self._n == 0

	def contains(self, i):
		return self._qp[i]  != -1

	def size(self):
		return self._n

	def insert(self, i, key):
		if (self.contains(i)):
			return None

		self._n += 1
		self._qp[i] = self._n
		self._pq[self._n] = i
		self._keys[i] = key
		self._swim(self._n)


	def min_index(self):
		return self._pq[1]


	def min_key(self):
		return self._keys[self._pq[1]]

	def del_min(self):
		min_index = self._pq[1]
		self._exch(1, self._n)
		self._n -= 1
		self._sink(1)
		assert(min_index == self._pq[self._n + 1])
		self._qp[min_index] = -1
		self._keys[min_index] = None
		self._pq[self._n+1] = -1
		return min_index

	def key_of(self, i):
		return self._keys[i]

	def change_key(self, i, key):
		self._keys[i] = key
		self._swim(self._qp[i])
		self._sink(self._qp[i])

	def delete(self, i):
		this_index = self._qp[i]
		self._exch(this_index, self._n)
		self._n -= 1
		self._swim(this_index)
		self._sink(this_index)
		self._keys[i] = None
		self._qp[i] = -1

	def _greater(self, i, j):
		return self._keys[self._pq[i]] > self._keys[self._pq[j]]

	def _exch(self, i, j):
		self._pq[i],self._pq[j] = self._pq[j], self._pq[i]
		self._qp[self._pq[i]] = i
		self._qp[self._pq[j]] = j


	def _swim(self, k):
		while k > 1 and self._greater(k // 2, k):
			self._exch(k, k // 2)
			k = k // 2

	def _sink(self, k):
		while (2*k <= self._n):
			j = 2 * k
			if j < self._n and self._greater(j , j + 1):
				j += 1
			if not self._greater(k , j):
				break
			self._exch(k, j)
			k = j

if __name__ == "__main__":
	nums = [9,5,2,6,3,4,7,1,8]
	pq = IndexMinPQ(100)
	for i in range(0, len(nums)):
		pq.insert(nums[i], str(nums[i]))

	while not pq.isEmpty():
		print(pq.del_min()) # 