from graph import Graph

class DepthFirstPaths:
	# find paths in graph G from given vertex s (source)
	def __init__(self, G, s):
		self._s = s
		self._edgeTo = [0] * G.V()
		self._marked = [False] * G.V()
		self._validate_vertex(s)
		self._dfs(G, s)

	# helper method to validate vertex v
	def _validate_vertex(self, v):
		V = len(self._marked)
		if v < 0 or v >= V:
			raise Exception ("Vertex " + str(v) + " is not between 0 and " + str(V))

	# is there a path from source to v
	def has_path_to(self, v):
		self._validate_vertex(v)
		return self._marked[v]

	# returns path from s to v if exists; returns null otherwise
	def path_to(self, v):
		self._validate_vertex(v)
		if not self.has_path_to(v):
			return None
		path = []
		x = v
		while x != self._s:
			path.append(x)
			x = self._edgeTo[x]
		path.append(self._s)
		return path

	def _dfs(self, G, v):
		self._marked[v] = True
		for w in G.adj(v):
			if not self._marked[w]:
				self._edgeTo[w] = v
				self._dfs(G , w)

if __name__ == "__main__":
	G = Graph(4)
	G.add_edge(0,3)
	G.add_edge(2,3)
	dfs_paths = DepthFirstPaths(G, 0)
	print(dfs_paths.has_path_to(1)) # False
	print(dfs_paths.has_path_to(2)) # True
	print(dfs_paths.has_path_to(3)) # True
	print(dfs_paths.path_to(2)) # [2, 3, 0]
	print(dfs_paths.path_to(3)) # [3, 0]
