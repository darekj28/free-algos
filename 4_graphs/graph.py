


class Graph:
	# Initializes an empty graph with V vertices and 0 edges.
	def __init__(self, V):
		self._V = V
		self._E = 0
		# initalizes an adjacency list for each vertex
		self._adj = [[] for i in range(0, V)]

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
		self._E += 1
		self._adj[v].append(u)
		self._adj[u].append(v)

	# returns all the neighbors of vertex v
	def adj(self, v):
		self._validate_vertex(v)
		return self._adj[v]


	def toString(self):
		return str(self._adj)

if __name__ == "__main__":
	V = 4
	G = Graph(V)
	G.add_edge(0,3)
	G.add_edge(0,2)
	print(G.adj(0)) # [3,2]
	print(G.toString()) # [[3, 2], [], [0], [0]]
