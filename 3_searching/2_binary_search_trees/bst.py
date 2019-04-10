import random 

class Node:
	def __init__(self, key , value, size):
		self.value = value
		self.key = key
		self.size = size
		self.left = None
		self.right = None

class BST:
	# create an empty binary search tree
	def __init__(self):
		self._root = None

	# put a key-value pair into the BST. 
	# Remove key from BST if value is None
	def put(self, key, value):
		if value is None:
			self.delete(key)
			return
		self._root = self._put(self._root, key, value)
		assert self.check()


	# helper method to insert into BST.
	# x is a node.
	def _put(self, x, key, value):
		if x is None:
			return Node(key, value, 1)
		if key < x.key:
			x.left = self._put(x.left, key , value)
		elif key > x.key:
			x.right = self._put(x.right, key, value)
		else:
			x.size = 1 + self.size(x.left) + self.size(x.right)
		return x



	# returns value paired with key. Returns None if key is absent
	def get(self, key):
		return self._get(self._root, key)

	# helper method for get function.
	# x is a Node
	def _get(self, x, key):
		if x is None:
			return None
		if key < x.key:
			return self._get(x.left, key)
		elif key > x.key:
			return self._get(x.right, key)
		else:
			return x.value

	# removes key and its value from the BST
	def delete(self, key):
		self._root = self._delete(root, key)
		assert self.check()

	# helper method for delete method.
	# x is a Node.
	def _delete(self, x, key):
		if x is None:
			return None
		if key < x.key:
			x.left = self._delete(x.left, key)
		elif key > x.key:
			x.right = self._delete(x.right, key)
		else:
			if x.right is None:
				return x.left
			if x.left is None:
				return x.right
			temp_node = x
			x = self.min(temp_node.right)
			x.right = self._delete_min(temp_node.right)
			x.left = temp_node.left
		x.size = self.size(x.left) + self.size(x.right) + 1
		return x

	# Returns a boolean indicating if there is a value paired with the key.
	def contains(self, key):
		return self.get(key) != None

	# Returns a boolean indicating if the BST is empty
	def isEmpty(self):
		return self.size() == 0

	# returns all keys in the BST
	def all_keys(self):
		return self.keys(self._root)

	# returns the key-value pairs rooted at Node x
	# defaults to whole tree if x is not specified
	def keys(self, x = None):
		if x is None:
			return []
		output_keys = []
		self._keys(x, output_keys)
		return output_keys

	# helper function for keys. x is a Node
	def _keys(self, x, output_keys):
		if x is None:
			return None
		self._keys(x.left, output_keys)
		output_keys.append(x.key)
		self._keys(x.right, output_keys)

	# Returns size of entire tree 
	def size(self):
		return self.node_size(self._root)

	# returns the size of the subtree rooted at Node x
	def node_size(self, x):
		if x == None:
			return 0
		return x.size

	# returns the smallest key
	def min(self):
		return self._min(root).key

	# helper method for min. 
	# x is a Node.
	def _min(self, x):
		if x.left is None:
			return x
		else:
			return self._min(x.left)


	# returns the largest key
	def max(self):
		return self._max(root).key

	# helper method for max. 
	# x is a Node.
	def _max(self, x):
		if x.right is None:
			return x
		else:
			return self._min(x.right)

	# returns the largest key less than or equal to key
	def floor(self, key):
		x = self._floor(self._root, key)
		if x is None:
			return None
		return x.key

	# helper method for floor
	# x is a Node 
	def _floor(self, x, key):
		if x is None:
			return None
		if key == x.key:
			return x
		elif key < x.key:
			return self._floor(x.left, key)
		temp_node = self._floor(x.right, key)
		if temp_node is not None:
			return temp_node
		else:
			return x

	# returns the smallest key larger than or equal to key
	def celing(self, key):
		x = self._ceiling(self._root, key)
		if x is None:
			return None
		else:
			return x.key

	# helper method for ceiling. x is a Node
	def _ceiling(self, x, key):
		if x is None:
			return None
		if key == x.key:
			return x
		elif key < x.key:
			temp_node = self._ceiling(x.left, key)
			if temp_node is not None:
				return temp_node
			else:
				return x
		return self._ceiling(x.right, key)

	# returns the number of keys less than key
	def rank(self, key):
		return self._rank(self._root, key)

	# helper function for rank. x is a Node
	def _rank(self, x, key):
		if x is None:
			return 0
		if key < x.key:
			return self._rank(x.left, key)
		elif key > x.key:
			return 1 + self.node_size(x.left) + self._rank(x.right, key)
		else:
			return self.node_size(x.left)


	# returns the key that has rank k
	def select(self, k):
		x = self._select(self._root, k)
		return x.key

	# helper function for select. x is a Node.
	def _select(self, x, k):
		if x is None:
			return None
		t = self.node_size(x.left)
		if t > k:
			return self._select(x.left, k)
		elif t < k:
			return self._select(x.right, k - t - 1)
		else:
			return x

	# deletes the smallest key
	def delete_min(self):
		self._root = self._delete_min(self._root)
		assert self.check()

	# helper method for delete_min. x is a Node.
	def _delete_min(self, x):
		if x.left is None:
			return x.right
		x.left = self._delete_min(x.left)
		x.size = self.size(x.left) + self.size(x.right) + 1
		return x

	# deletes the largest key
	def delete_max(self):
		self._root = self._delete_max(self._root)
		assert self.check()

	# helper method for delete_max. x is a Node
	def _delete_max(self, x):
		if x.right is None:
			return x.left
		x.right = self._delete_max(x.right)
		x.size = self.size(x.left) + self.size(x.right) + 1
		return 

	# check if BST is valid.
	def check(self):
		return self._check(self._root, None, None)

	# helper function for check. x is a Node
	def _check(self, x, min_key, max_key):
		if x is None:
			return True
		if min_key and x.key <= min_key:
			return False
		if max_key and x.key >= max_key:
			return False
		return self._check(x.left, min_key, x.key) and self._check(x.right, x.key, max_key)

	def level_order(self):
		keys = []
		queue = []
		queue.append(self._root)
		while queue:
			x = queue.pop(0)
			if x is None:
				continue
			keys.append(x.key)
			queue.append(x.left)
			queue.append(x.right)
		return keys
		

if __name__ == "__main__":
	st = BST()
	input_list = range(0, 8)
	random.shuffle(input_list)
	for num in input_list:
		st.put(str(num), num)

	for s in st.level_order():
		print(s, st.get(s))

	print("\n")

	for s in st.all_keys():
		print(s, st.get(s))












