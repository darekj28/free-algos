import random

RED = True
BLACK = False

class Node:
	def __init__(self, key, value, color, size):
		self.key = key 
		self.value = value
		self.color = color
		self.left = None
		self.right = None
		self.size = size

class RedBlackBST:
	# constructs a RB BST
	def __init__(self):
		self._root = None


	# is the node x red? x is a Node.
	def _is_red(self, x):
		if x is None:
			return False
		return x.color == RED

	# return the number of node in the subtree rooted at x; 0 if x is None
	def _size(self, x):
		if x is None:
			return 0
		return x.size

	# returns the number of key-value pairs in the tree
	def size(self):
		return self._size(self._root)

	# Returns a boolean indicating if the BST is empty
	def isEmpty(self):
		return self.size() == 0



	# returns value paired with key. Returns None if key is absent
	def get(self, key):
		return self._get(self._root, key)

	# helper method for get function.
	# x is a Node
	def _get(self, x, key):
		while x is not None:
			if key < x.key:
				x = x.left
			elif key > x.key:
				x = x.right
			else:
				return x.value
		return None

	# Returns a boolean indicating if there is a value paired with the key.
	def contains(self, key):
		return self.get(key) != None


	# put a key-value pair into the BST. 
	# Remove key from BST if value is None
	def put(self, key, value):
		if value is None:
			self.delete(key)
			return

		self._root = self._put(self._root, key, value)
		self._root.color = BLACK
		self.check()


	# helper method to insert into BST.
	# x is a node.
	def _put(self, x, key, value):
		if x is None:
			return Node(key, value, RED, 1)
		if key < x.key:
			x.left = self._put(x.left, key , value)
		elif key > x.key:
			x.right = self._put(x.right, key, value)
		else:
			x.value = value

		if self._is_red(x.right) and not self._is_red(x.left):
			x = self._rotate_left(x)
		if self._is_red(x.left) and self._is_red(x.left.left):
			x = self._rotate_right(x)
		if self._is_red(x.left) and self._is_red(x.right):
			self._flip_colors(x)
		x.size = self._size(x.left) + self._size(x.right) + 1
		return x

	# deletes the smallest key
	def delete_min(self):
		assert self.size() > 0
		if  self._is_red(root.left) == False and self._is_red(root.right) == False:
			self._root.color = RED
		self._root = self._delete_min(root)
		if  self.isEmpty() == False:
			self._root.color = BLACK

		self.check()

	# helper method for delete_min. x is a Node.
	def _delete_min(self, x):
		if x.left is None:
			return None
		if  self._is_red(x.left) == False  and self._is_red(x.left.left) == False:
			x = self._move_red_left(x)

		x.left = self.delete_min(x.left)
		return self._balance(x)

	# deletes the largest key
	def delete_max(self):
		assert self.size() > 0
		if self._is_red(root.left) == False and self._is_red(root.right) == False:
			self._root.color = RED
		self._root = self._delete_max(self._root)
		if self.isEmpty() == False:
			self._root.color = BLACK
		self.check()

	# helper method for delete_max. x is a Node
	def _delete_max(self, x):
		if self._is_red(x.left):
			x = self._rotate_right(x)
		if x.right is None:
			return None
		if self._is_red(x.right) == False and self._is_red(x.right.left) == False:
			x = self._move_red_right(x)
		x.right = self._delete_max(x.right)
		return self._balance(x)


	# removes key and its value from the BST
	def delete(self, key):
		if self.contains(key) == False:
			return None

		if self._is_red(self._root.left) == False and self._is_red(self._root.right) == False:
			self._root.color = RED
		self._root = self._delete(self._root, key)
		if self.isEmpty() == False:
			self._root.color = BLACK
		self.check()

	# helper method for delete method.
	# x is a Node.
	def _delete(self, x, key):
		if key < x.key:
			if self._is_red(x.left) == False and self._is_red(x.left.left) == False:
				x = self._move_red_left(x)
			x.left = self._delete(x.left, key)

		else:
			if self._is_red(x.left):
				x = self._rotate_right(x)
			if key == x.key and x.right is None:
				return None
			if self._is_red(x.right) == False and self._is_red(x.right.left) == False:
				x = self._move_red_right(x)
			if key == x.key:
				temp_node = self._min(x.right)
				x.key = temp_node.key
				x.value = temp_node.value
				x.right = self._delete_min(x.right)
			else:
				x.right = self._delete(x.right, key)
		return self._balance(x)

	"""
		Red-black tree helper functions
	"""

	# make a left-leaning link lean to the right
	def _rotate_right(self, h):
		x = h.left
		h.left = x.right
		x.right = h;
		x.color = x.right.color;
		x.right.color = RED;
		x.size = h.size;
		h.size = self._size(h.left) + self._size(h.right) + 1;
		return x

	# make a right-leaning link lean to the left
	def _rotate_left(self, h):
		x = h.right;
		h.right = x.left;
		x.left = h;
		x.color = x.left.color;
		x.left.color = RED;
		x.size = h.size;
		h.size = self._size(h.left) + self._size(h.right) + 1;
		return x
   

	# flip the colors of a node and its two children
	def _flip_colors(self, h):
		# h must have opposite color of its two children
		# assert (h != null) && (h.left != null) && (h.right != null);
		h.color = not h.color;
		h.left.color =  not h.left.color;
		h.right.color = not h.right.color;

	# Assuming that h is red and both h.left and h.left.left
	# are black, make h.left or one of its children red.
	def _move_red_left(self, h):
		# assert (h != null);
		# assert is_red(h) && !is_red(h.left) && !is_red(h.left.left);

		self._flip_colors(h);
		if self._is_red(h.right.left):
			h.right = self._rotate_right(h.right)
			h = self._rotate_left(h)
			self._flip_colors(h)
		return h

	# Assuming that h is red and both h.right and h.right.left
	# are black, make h.right or one of its children red.
	def _move_red_right(self, h):
		# assert (h != null);
		# assert is_red(h) && !is_red(h.right) && !is_red(h.right.left);
		self._flip_colors(h);
		if self._is_red(h.left.left):
			h = self._rotate_right(h)
			self._flip_colors(h)

		return h

	# restore red-black tree invariant
	def _balance(self, h):
		assert h != None

		if self._is_red(h.right): 
			h = self._rotate_left(h)
		if self._is_red(h.left) and self._is_red(h.left.left):
			h = self._rotate_right(h)
		if self._is_red(h.left) and self._is_red(h.right):
			self._flip_colors(h);

		h.size = self._size(h.left) + self._size(h.right) + 1;
		return h

	def height(self):
		return self._height(self._root)

	def _height(self, x):
		if x is None:
			return -1
		return 1 + max(self._height(x.left), self._height(x.right))

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
		

	"""
		Check integreity of red black tree structure
	"""

	def check(self):
		assert self._is_BST(self._root, None, None)
		assert self._is_size_consistent(self._root)
		assert self._is_rank_consistent(self._root)
		assert self._is_23(self._root)
		num_black = 0
		x = self._root
		while x is not None:
			if self._is_red(x) == False:
				num_black += 1
			x = x.left
		assert self._is_balanced(self._root, num_black)

	# does this binary tree satisfy symmetric order?
	def _is_BST(self, x, min_key, max_key):
		if x is None:
			return True
		if min_key and x.key <= min_key:
			return False
		if max_key and x.key >= max_key:
			return False
		return self._is_BST(x.left, min_key, x.key) and self._is_BST(x.right, x.key, max_key)

	# are the size fields correct?
	def _is_size_consistent(self, x):
		if x is None:
			return True
		if x.size != self._size(x.left) + self._size(x.right) + 1:
			return False
		return self._is_size_consistent(x.left) and self._is_size_consistent(x.right)

	# check that the ranks are consistent
	def _is_rank_consistent(self, x):
		for i in range(0, self.size()):
			if i != self.rank(self.select(i)):
				return False
		for key in self.all_keys():
			if key != self.select(self.rank(key)):
				return False
		return True

	# Does the tree have no red right links, and at most one (left)
	# red links in a row on any path?
	def _is_23(self, x):
		if x is None:
			return True
		if self._is_red(x.right):
			return False
		if x != self._root and self._is_red(x) and self._is_red(x.left):
			return False
		return self._is_23(x.left) and self._is_23(x.right)

	# does every path from the root to a leaf have the given number of black links?
	def _is_balanced(self, x, num_black):
		if x is None:
			return num_black == 0
		if self._is_red(x) == False:
			num_black -= 1
		return self._is_balanced(x.left, num_black) and self._is_balanced(x.right, num_black)


if __name__ == "__main__":
	st = RedBlackBST()
	input_list = range(0, 8)
	random.shuffle(input_list)
	for num in input_list:
		st.put(str(num), num)

	for s in st.level_order():
		print(s, st.get(s))
	print()
	for s in st.all_keys():
		print(s, st.get(s))
		st.delete(s)



		
