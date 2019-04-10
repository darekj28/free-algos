

class Node:
	def __init__(self, key, value, next):
		self.key = key
		self.value = value
		self.next = next

class BinarySearchST:
	# create an empty binary search symbol table
	def __init__(self, capacity = 10):
		self._n = 0
		self._keys = [None] * capacity
		self._vals = [None] * capacity


	def _resize(self, capacity):
		assert capacity >= self._n
		tempk = None * [capacity]
		tempv = None * [capacity]
		for i in range(0, self._n):
			tempv[i] = self._vals[i]
			tempk[i] = self._keys[i]
		self._vals = tempv
		self._keys = tempk

	# put a key-value pair into the table. Remove key from table if value is None
	def put(self, key, value):
		if value is None:
			self.delete(key)
			return 
		i = self.rank(key)

		if i < self._n and self._keys[i] == key:
			self._vals[i] = value
			return

		if self._n == len(self._keys):
			self._resize(2 * len(self._keys))

		for j in range(self._n, i)[::-1]:
			self._keys[j] = self._keys[j-1]
			self._vals[j] = self._vals[j-1]

		self._keys[i] = key
		self._vals[i] = value
		self._n += 1


	# returns value paired with key. Returns None if key is absent
	def get(self, key):
		if self.isEmpty():
			return None
		i = self.rank(key)
		if i < self._n and self._keys[i] == key:
			return self._vals[i]
		return None

	# removes key and its value from the symbol table
	def delete(self, key):
		if self.isEmpty():
			return
		i = self.rank(key)

		if i == self._n or self._keys[i] != i:
			return

		for j in range(i, n-1):
			self._keys[j] = self._keys[j+1]
			self._vals[j] = self._vals[j+1]
		n -= 1
		self._keys[n] = None
		self._vals[n] = None

		if self._n > 0 and self._n == len(self._keys) / 4:
			self._resize(len(self._keys) // 2)
		

	# Returns a boolean indicating if there is a value paired with the key.
	def contains(self, key):
		return self.get(key) is not None

	# Returns a boolean indicating if the table is empty
	def isEmpty(self):
		return self._n == 0

	# returns a list of all keys in the table between lo and hi
	def keys(self, lo = None, hi = None):
		if lo is None:
			lo = self.min()
		if hi is None:
			hi = self.max()
		output_keys = []
		if lo  > hi:
			return output_keys
		i = self.rank(lo)
		while i < self.rank(hi):
			output_keys.append(self._keys[i])
			i += 1
		return output_keys

	# returns the number of key value pairs
	# returns the number of keys between lo and hi where lo,hi are keys
	def size(self, lo = None, hi = None):
		if lo is None:
			min_key = self.min()
		if hi is None:
			max_key = self.max()
		if lo  > hi:
			return 0
		if self.contains(hi):
			return self.rank(hi) - self.rank(lo) + 1
		else:
			return self.rank(hi) - self.rank(lo)

	# returns the smallest key
	def min(self):
		return self._keys[0]

	# returns the largest key
	def max(self):
		return self._keys[self._n - 1]

	# returns the largest key less than or equal to key
	def floor(self, key):
		i = self.rank(key)
		if i < self._n and key == self._keys[i]:
			return self._keys[i]
		if i == 0:
			return None
		else:
			return self._keys[i-1]

	# returns the smallest key larger than or equal to key
	def celing(self, key):
		i = self.rank(key)
		if i == n:
			return None
		else:
			return self._keys[i]

	# returns the number of keys strictly less than key
	def rank(self, key):
		lo = 0
		hi = self._n - 1
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if key < self._keys[mid]:
				hi = mid - 1
			elif key > self._keys[mid]:
				lo = mid + 1
			else:
				return mid
		return lo

	# returns the key that has rank k
	def select(self, k):
		return self._keys[k];

	# deletes the smallest key
	def delete_min(self):
		self.delete(self.min())

	# deletes the largest key
	def delete_max(self):
		self.delete(self.max())    	

if __name__ == "__main__":
	st = BinarySearchST(capacity = 30)
	for i in range(0, 10):
		st.put(str(i), i)

	for key in st.keys():
		print(key, st.get(key))



	