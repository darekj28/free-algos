# Don't change this! 

class WeightedQuickFindUF:
	# initialize N sites with integer names (0 to N-1)
	def __init__(self, N):
		assert N > 0
		self._count = N
		self._parent = [i for i in range(N)]
		self._size = [1] * N

	# private function to validate that p is valid index
	def _validate(self, p):
		n = len(self._parent)
		assert p >= 0 and p < n


	# add connection between p and q
	def union(self, p, q):
		self._validate(p)
		self._validate(q)
		rootP = self.find(p)
		rootQ = self.find(q)
		if rootP == rootQ:
			return
		
		if self._size[rootP] < self._size[rootQ]:
			self._parent[rootP] = rootQ
			self._size[rootQ] += self._size[rootP]
		else:
			self._parent[rootQ] = rootP
			self._size[rootP] += self._size[rootQ]
		self._count -= 1


	# component identifier for p (0 to N-1)
	def find(self, p):
		self._validate(p)
		root = p
		while root != self._parent[root]:
			root = self._parent[root]
			self._parent[p] = root
		while(p != root):
			next = self._parent[p]
			self._parent[p] = root
			p = next
		return p

	# return true if p and q are in the same component
	def connected(self, p, q):
		self._validate(p)
		self._validate(q)
		return self.find(p) == self.find(q)

	# returns the number of components
	def count(self):
		return self._count


if __name__ == "__main__":
	N = 8
	uf = WeightedQuickFindUF(N)
	print(uf.count()) # 8
	uf.union(0,4) 
	print(uf.count()) # 7
	uf.union(0,3)
	print(uf.count()) # 6
	uf.union(3,4)
	print(uf.count()) # 6
	print(uf.find(5)) # 5
	uf.union(4,5)
	print(uf.count()) # 5
	print(uf.find(5)) # 0 





