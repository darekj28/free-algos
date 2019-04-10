import random
from sequential_search_st import SequentialSearchST


class SeparateChainingHashST:
	_INIT_CAPACITY = 10
	# initializes an empty hash table
	def __init__(self, num_chains = None):
		if num_chains is None:
			num_chains = self._INIT_CAPACITY
		# number of elements in the table
		self._n = 0 
		# number of chains in the hash table
		self._m = num_chains
		# list containing sepearate chains
		self._st = []
		for i in range(0, self._m):
			self._st.append(SequentialSearchST())

	# resize the hash table to have the given number of chains
	# then rehash all the previous keys.
	def _resize(self, num_chains):
		temp = SeparateChainingHashST(num_chains)
		for i in range(0, self._m):
			for key in self._st[i].keys():
				temp.put(key, self._st[i].get(key))

		self._m = temp._m
		self._n = temp._n
		self._st = temp._st

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
		return self._st[i].get(key)

	# Inserts the specified key-value pair into the symbol table, overwriting the old 
	# value with the new value if the symbol table already contains the specified key.
	# Deletes the specified key (and its associated value) from this symbol table
	# if the specified value is None
	def put(self, key, value):
		if value is None:
			self.delete(key)
			return
		# double the table size if the average list length is >= 10
		if self._n >= 10 * self._m:
			self._resize(2 * self._m)

		i = self._hash(key)
		if self._st[i].contains(key) == False:
			self._n += 1
		self._st[i].put(key, value)

	# Removes the specified key and its associated value from this symbol table     
	# (if the key is in this symbol table).    
	def delete(self, key):
		i = self._hash(key)
		if self._st[i].contains(key):
			self._n -= 1

		self._st[i].delete(key)

		# halve table size if average length of list <= 2
		if self._m > self._INIT_CAPACITY and self._n <= 2*self._m:
			self._resize(self._m // 2)


	# returns list of keys in the hash table
	def keys(self):
		output_keys = []
		for i in range(0, self._m):
			for key in self._st[i].keys():
				output_keys.append(key)
		return output_keys




if __name__ == "__main__":
	st = SeparateChainingHashST()
	input_list = range(0, 256)
	random.shuffle(input_list)
	for num in input_list:
		st.put(str(num), num)

	for s in st.keys():
		print(s, st.get(s))
		st.delete(s)



