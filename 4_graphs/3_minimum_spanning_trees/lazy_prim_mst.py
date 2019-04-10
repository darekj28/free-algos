from min_pq import MinPQ
from edge import Edge
from edge_weighted_graph import EdgeWeightedGraph

class LazyPrimMST:
	# Compute a minimum spanning tree (or forest) of an edge-weighted graph.
    #the edge-weighted graph
	def __init__(self, G):
		self._mst = []
		self._pq = MinPQ(G.V())
		self._marked = [False] * G.V()
		self._weight = 0
		for v in range(0, G.V()):
			if not self._marked[v]:
				self._prim(G, v)

	# run Prim's algorithm 
	def _prim(self, G, s):
		self._scan(G, s)
		while not self._pq.isEmpty():
			e = self._pq.del_min()
			v = e.either()
			w = e.other(v)
			assert(self._marked[v] or self._marked[w])
			if (self._marked[v] and self._marked[w]):
				continue
			self._mst.append(e)
			self._weight += e.weight()
			if not self._marked[v]:
				self._scan(G, v)
			if not self._marked[w]:
				self._scan(G, w)


	# add all edges e incident to v onto pq if the other endpoint has not yet been scanned
	def _scan(self, G, v):
		assert not self._marked[v]
		self._marked[v] = True
		for e in G.adj(v):
			if not self._marked[e.other(v)]:
				self._pq.insert(e)

	def weight(self):
		return self._weight

	def edges(self):
		return self._mst


if __name__ == "__main__":
	V = 3
	G = EdgeWeightedGraph(V)
	edge_1 = Edge(0,1,4.4)
	edge_2 = Edge(0,2, 3.3)
	big_edge = Edge(1,2, 10000)
	G.add_edge(edge_1)
	G.add_edge(edge_2)
	G.add_edge(big_edge)
	lazy_prim = LazyPrimMST(G)
	print(lazy_prim.edges()) # [(0, 2, 3.3), (0, 1, 4.4)]
	print(lazy_prim.weight()) # 7.7


