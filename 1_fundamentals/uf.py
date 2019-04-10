

class UF:
	# initialize N sites with integer names (0 to N-1)
	def __init__(self, N):
		assert N > 0
		self._count = N
		self._parent = [0] * N
		self._rank = [0] * N
		for i in range(0, N):
			self._parent[i] = i
			self._rank[i] = 0

	# private function to validate that p is valid index
	def _validate(self, p):
		n = len(self._parent)
		assert p >= 0 and p < n


	# add connection between p and q
	def union(self, p, q):
		rootP = self.find(p)
		rootQ = self.find(q)
		if rootP == rootQ:
			return 
		if self._rank[rootP] < self._rank[rootQ]:
			self._parent[rootP] = rootQ
		elif self._rank[rootP] > self._rank[rootQ]:
			self._parent[rootQ] = rootP
		else:
			self._parent[rootQ] = rootP
			self._rank[rootP] += 1
		self._count -= 1


	# component identifier for p (0 to N-1)
	def find(self, p):
		self._validate(p)
		while p != self._parent[p]:
			self._parent[p] = self._parent[self._parent[p]]
			p = self._parent[p]
		return p

	# return true if p and q are in the same component
	def connected(self, p, q):
		return self.find(p) == self.find(q)

	# returns the number of components
	def count(self):
		return self._count


if __name__ == "__main__":
	N = 8
	uf = UF(N)
	print(uf.count()) # 8
	uf.union(0,4) 
	print(uf.count()) # 7
	uf.union(0,3)
	print(uf.count()) # 6
	uf.union(3,4)
	print(uf.count()) # 6
	print(uf.find(5)) # 5
	uf.union(4,5)
	print(uf.find(5)) # 0 





