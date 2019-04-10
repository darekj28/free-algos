import random



class LinearProbingHashST:
	_INIT_CAPACITY = 10
	# initializes an empty hash table
	def __init__(self, m = None):
		if m is None:
			m = self._INIT_CAPACITY
		# number of elements in the table
		self._n = 0 
		# number of chains in the hash table
		self._m = m
		# list containing sepearate chains
		self._keys = [None] * self._m
		self._vals = [None] * self._m

	# resize the hash table to have the given the new capacity
	# then rehash all the previous keys.
	def _resize(self, capacity):
		temp = LinearProbingHashST(capacity)
		for i in range(0, self._m):
			if self._keys[i] is not None:
				temp.put(self._keys[i], self._vals[i])

		self._keys = temp._keys
		self._vals = temp._vals
		self._m = temp._m
		self._n = temp._n

	# hash the value between 0 and m-1
	def _hash(self, key):
		return (hash(key) & 0x7fffffff) % self._m

	# returns the number of key-value paris in this hash table
	def size(self):
		return self._n

	# returns True if the hash table is empty
	def isEmpty(self):
		return self.size() == 0

	# returns True if this hash table contains the specified key.
	def contains(self, key):
		return (self.get(key) is not None)

	# Returns the value associated with the specified key in this symbol table.
	def get(self, key):
		i = self._hash(key)
		while self._keys[i] is not None:
			if self._keys[i] == key:
				return self._vals[i]
			i = (i + 1) % m
		return None

	# Inserts the specified key-value pair into the symbol table, overwriting the old 
	# value with the new value if the symbol table already contains the specified key.
	# Deletes the specified key (and its associated value) from this symbol table
	# if the specified value is None
	def put(self, key, value):
		if value is None:
			self.delete(key)
			return

		# double the table size if it's 50% full
		if self._n >=  self._m // 2:
			self._resize(2 * self._m)

		i = self._hash(key)
		while self._keys[i] is not None:
			if self._keys[i] == key:
				self._vals[i] = value
				return
			i = (i + 1) % self._m

		self._keys[i] = key
		self._vals[i] = value
		self._n += 1

	# Removes the specified key and its associated value from this symbol table     
	# (if the key is in this symbol table).    
	def delete(self, key):
		if self.contains(key) == False:
			return 
		i = self._hash(key)
		while self._keys[i] != key:
			i = (i + 1) % self._m

		self._keys[i] = None
		self._vals[i] = None

		i = (i + 1) % self._m
		# rehash all keys in same cluster
		while self._keys[i] is not None:
			# delete keys[i] and vals[i] and reinsert
			key_to_rehash = self._keys[i]
			val_to_rehash = self._keys[i]
			self._keys[i] = None
			self._vals[i] = None
			self._n -= 1
			self.put(key_to_rehash, val_to_rehash)
			i = (i + 1) % self._m

		self._n -= 1

		# halve table size if it's 12.5% full or less
		if self._n > 0 and self._n <= self._m // 8:
			self._resize(self._m // 2)


	# returns list of keys in the hash table
	def keys(self):
		output_keys = []
		for i in range(0, self._m):
			if self._keys[i] is not None:
				output_keys.append(self._keys[i])
		return output_keys


if __name__ == "__main__":
	st = LinearProbingHashST()
	input_list = range(0, 256)
	random.shuffle(input_list)
	for num in input_list:
		st.put(str(num), num)

	for s in st.keys():
		print(s, st.get(s))
		st.delete(s)



