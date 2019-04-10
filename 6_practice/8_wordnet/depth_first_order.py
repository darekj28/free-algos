from digraph import Digraph

class DepthFirstOrder:
	# Determines a depth-first order for the digraph G
	# treats 0 as the source node
	def __init__(self, G):
		self._pre_counter = 0
		self._post_counter = 0
		self._pre = [0] * G.V()
		self._post = [0] * G.V()
		self._postorder = [] 
		self._preorder = []
		self._marked = [False] * G.V()
		for v in range(0, G.V()):
			if not self._marked[v]:
				self._dfs(G,v)

	# performs dfs given a graph G and vertex v
	def _dfs(self, G, v):
		self._marked[v] = True
		self._pre_counter + 1
		self._pre[v] = self._pre_counter
		self._preorder.append(v)
		for w in G.adj(v):
			if not self._marked[w]:
				self._dfs(G, w)
		self._postorder.append(v)
		self._post_counter += 1
		self._post[v] = self._post_counter

	# returns the preorder number of vertex v
	def pre(self, v):
		return self._pre[v]

	# returns the postorder number of vertex v
	def post(self, v):
		return self._post[v]


	# rerurns the vertices in postorder from 0
	def postorder(self):
		return self._postorder

	# rerurns the vertices in preorder from 0
	def preorder(self):
		return self._preorder

	# returns reverse postorder from 0
	def reverse_postorder(self):
		return self._postorder[::-1]

if __name__ == "__main__":
	G = Digraph(4)
	G.add_edge(0,3)
	G.add_edge(3,2)
	orders = DepthFirstOrder(G)
	print(orders.postorder())  # [2, 3, 0, 1]
	print(orders.reverse_postorder()) # [1, 0, 3, 2]
	print(orders.preorder()) # [0, 3, 2, 1]

