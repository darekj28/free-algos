

class QuickFindUF:
	# initialize N sites with integer names (0 to N-1)
	def __init__(self, N):
		assert N > 0
		self._id = range(0, N)
		self._count = N

	# private function to validate that p is valid index
	def _validate(self, p):
		n = len(self._id)
		assert p >= 0 and p < n


	# add connection between p and q
	def union(self, p, q):
		self._validate(p)
		self._validate(q)
		pID = self._id[p]
		qID = self._id[q]
		
		# if p and q are already in the same component
		if pID == qID:
			return

		for i in range(0, len(self._id)):
			if self._id[i] == pID:
				self._id[i] = qID

		self._count -= 1


	# component identifier for p (0 to N-1)
	def find(self, p):
		self._validate(p)
		return self._id[p]

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
	uf = QuickFindUF(N)
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





