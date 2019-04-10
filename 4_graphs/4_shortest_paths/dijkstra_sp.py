
from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge

from index_min_pq import IndexMinPQ

class DijktstraSP:
	# initializes a shortest path given an EdgeWeightedDigraph G and a source vertex s
	def __init__(self, G, s):
		self._distTo = [float('infinity')] * G.V()
		self._edgeTo = [None] * G.V()
		self._distTo[s] = 0
		self._pq = IndexMinPQ(G.V())
		self._pq.insert(s, self._distTo[s])
		while not self._pq.isEmpty():
			v = self._pq.del_min()
			for e in G.adj(v):
				self._relax_edge(e)


	# returns shortest distance from s to v. Returns infinity if no path exists.
	def dist_to(self, v):
		return self._distTo[v]

	# returns a boolean indicating if there exists a path from s to v
	def has_path_to(self, v):
		return (self._distTo[v] != float('infinity'))

	# returns the shortest path from s to v as a list of vertices. Returns null if there is no path
	def path_to(self, v):
		path = []
		e = self._edgeTo[v]
		while e:
			path.append(e)
			e = self._edgeTo[e.from_vertex()]
		return path

	# helper function in SP to relax DirectedEdge e 
	def _relax_edge(self , e):
		v = e.from_vertex()
		w = e.to_vertex()
		if self._distTo[w] > (self._distTo[v] + e.weight()):
			self._distTo[w] = self._distTo[v] + e.weight()
			self._edgeTo[w] = e

	# helper function in SP to relax vertex v in an EdgeWeightedDigraph G  
	def _relax_vertex(G, v):
		for e in G.adj(v):
			w = e.to_vertex()
			if self._distTo[w] > (self._distTo[v] + e.weight()):
				self._distTo[w] = self._distTo[v] + e.weight()
				self._edgeTo[w] = e

if __name__ == "__main__":
	V = 5
	G = EdgeWeightedDigraph(V)
	edge_1 = DirectedEdge(0,1, 2.2)
	edge_2 = DirectedEdge(1,2, 3.3)
	edge_3 = DirectedEdge(2,3, 5.55)
	edge_4 = DirectedEdge(0,3, 7.1)
	G.add_edge(edge_1)
	G.add_edge(edge_2)
	G.add_edge(edge_3)
	G.add_edge(edge_4)

	sp = DijktstraSP(G, 0)

	print(sp.has_path_to(3)) # True
	print(sp.path_to(3)) # [0, 3, 7]
	print(sp.dist_to(3)) # [7.1]
	print(sp.has_path_to(4)) # False