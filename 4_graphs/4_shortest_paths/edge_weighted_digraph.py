from directed_edge import DirectedEdge

class EdgeWeightedDigraph:
    # create an empty V-vertex EdgeWeightedGraph
    # using adjacency list representation
    def __init__(self, V):
    	self._V = V
    	self._E = 0
    	self._adj = []
    	for v in range(0, V):
    		self._adj.append([])

    # returns number of vertices in this EdgeWeightedGraph
    def V(self):
    	return self._V

    # returns number of edges in this EdgeWeightedGraph
    def E(self):
    	return self._E

    # add edge e to this EdgeWeightedGraph
    def add_edge(self, e):
    	v = e.from_vertex()
    	w = e.to_vertex()
    	self._adj[v].append(e)
    	self._E += 1

    # returns edges adjacent to vertex v in this EdgeWeightedGraph
    def adj(self, v):
    	return self._adj[v]

    # returns all edges in this EdgeWeightedGraph
    def edges(self):
    	all_edges = set()
    	for v in range(0, self._V):
    		for e in self._adj(v):
    			all_edges.add(e)
    	return all_edges

    def toString(self):
		return str(self._adj)


if __name__ == "__main__":
	V = 4
	G = EdgeWeightedDigraph(V)
	edge_1 = DirectedEdge(0,3,4.4)
	edge_2 = DirectedEdge(0,2, 3.3)
	G.add_edge(edge_1)
	G.add_edge(edge_2)
	print(G.adj(0)) # [(0, 3, 4.4), (0, 2, 3.3)]
	print(G.toString()) # [[(0, 3, 4.4), (0, 2, 3.3)], [], [], []]