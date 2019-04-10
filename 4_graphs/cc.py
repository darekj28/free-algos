from graph import Graph

class CC:
    # contructor takes in a graph G
    def __init__(self, G):
    	# count is the number of connected coponents in the graph
    	self._count = 0
    	self._marked = [False] * G.V()
    	self._id = [0] * G.V()
    	# size of each component
    	self._size = [0] * G.V()
    	for v in range(0, G.V()):
    		if not self._marked[v]:
    			self._dfs(G, v)
    			self._count += 1

    # performs DFS for the graph on v
    def _dfs(self, G, v):
    	self._marked[v] = True
    	self._id[v] = self._count
    	self._size[self._count] = self._size[self._count] + 1
    	for w in G.adj(v):
    		if not self._marked[w]:
    			self._dfs(G, w)


    #  returns a boolean indicating if v, w are connected
    def connected(self, v, w):
    	return self._id[v] == self._id[w]

    # returns the number of connected components
    def count(self):
    	return self._count

    # component identifier for v
    def id(self, v):
    	return self._id[v]


if __name__ == "__main__":
	G = Graph(4)
	G.add_edge(0,3)
	G.add_edge(2,3)
	cc = CC(G)
	print(cc.count()) # 2
	print(cc.connected(0, 1)) # False
	print(cc.connected(0, 2)) # True