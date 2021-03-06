


class Digraph:
	# Initializes an empty graph with V vertices and 0 edges.
	def __init__(self, V):
		self._V = V
		self._E = 0
		# initalizes an adjacency list for each vertex
		self._adj = []
		for i in range(0,V):
			self._adj.append([False] * V)

	# returns the number of vertices in this graph
	def V(self):
		return self._V

	# returns the number of edges in this graph
	def E(self):
		return self._E

	# helper function to validate vertices
	def _validate_vertex(self, v):
		if v < 0 or v >= self._V:
			raise Exception("vertex " + str(v) + " is not between 0 and " + str((self._V-1)))


	# add edge between u-v in this graph, u,v are vertices
	def add_edge(self, u, v):
		self._validate_vertex(u)
		self._validate_vertex(v)
		if not self._adj[u][v]:
			self._E += 1

		self._adj[u][v] = True

	# returns all the neighbors of vertex v
	def adj(self, v):
		self._validate_vertex(v)
		neighbors = []
		for u in range(0, self._V):
			if self._adj[v][u]:
				neighbors.append(u)
		return neighbors

	# returns a Digraph that is the reverse of this Digraph
	def reverse(self):
		reverse_G = Digraph(self._V)
		for v in range(0, self._V):
			for w in self.adj(v):
				reverse_G.add_edge(w, v)
		return reverse_G


	def toString(self):
		s = ""
		for row in self._adj:
			s += str(row) + "\n"
		return s


if __name__ == "__main__":
	V = 4
	G = Digraph(V)
	G.add_edge(0,3)
	G.add_edge(0,1)
	G.add_edge(3,2)
	reverse_G = G.reverse()
	print(G.adj(0)) # 3, 1 
	print(G.toString())
	"""
	[False, True, False, True]
	[False, False, False, False]
	[False, False, False, False]
	[False, False, True, False]
	"""
	print(reverse_G.toString())
	"""
	[False, False, False, False]
	[True, False, False, False]
	[False, False, False, True]
	[True, False, False, False]
	"""


