

class Node:
	def __init__(self, key, value, next):
		self.key = key
		self.value = value
		self.next = next

class SequentialSearchST:
	# create an empty symbol table
	def __init__(self):
		self._n = 0
		self._first = None

	# put a key-value pair into the table. Remove key from table if value is None
	def put(self, key, value):
		if value is None:
			self.delete(key)
			return 
		x = self._first
		while x is not None:
			if key == x.key:
				x.value = value
				return
			x = x.next


		self._first = Node(key, value, self._first)
		self._n += 1


	# returns value paired with key. Returns None if key is absent
	def get(self, key):
		x = self._first
		while x is not None:
			if key == x.key:
				return x.value
			x = x.next
		return None

	# removes key and its value from the symbol table
	def delete(self, key):
		first = self._delete(self._first, key)

	# helper function to delete nodes
	def _delete(self, x, key):
		if x is None:
			return None
		if key == x.key:
			self._n -= 1
			return x.next
		x.next = self._delete(x.next, key)
		return x

	# Returns a boolean indicating if there is a value paired with the key.
	def contains(self, key):
		return self.get(key) is not None

	# Returns a boolean indicating if the table is empty
	def isEmpty(self):
		return self.size() == 0

	# returns a list of all keys in the table
	def keys(self):
		output_keys = []
		x = self._first
		while x is not None:
			output_keys.append(x.key)
			x = x.next
		return output_keys

	# returns the size of the table
	def size(self):
		return self._n

if __name__ == "__main__":
	st = SequentialSearchST()
	for i in range(0, 10):
		st.put(str(i), i)

	for key in st.keys():
		print(st.get(key))



	