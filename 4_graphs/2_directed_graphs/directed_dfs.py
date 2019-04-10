from digraph import Digraph

class DirectedDepthFirstSearch:
    # find vertices in graph G connected to vertex s (source)
    def __init__(self, G, s): 
    	self._marked = [False] * G.V()
    	self._count = 0
    	self._validate_vertex(s)
    	self._dfs(G, s)

    # helper method to validate vertex v
    def _validate_vertex(self, v):
    	V = len(self._marked)
    	if v < 0 or v >= V:
    		raise Exception ("Vertex " + str(v) + " is not between 0 and " + str(V))

    # Performs depth first serach starting from v
    def _dfs(self, G, v):
    	self._count += 1
    	self._marked[v] = True
    	for w in G.adj(v):
    		if not self._marked[w]:
    			self._dfs(G, w)

    # returns True if v is connected to s and False otherwise
    def marked(self, v):
    	self._validate_vertex(v)
    	return self._marked[v]

    # returns number of vertices connected to s
    def count(self):
    	return self._count


if __name__ == "__main__":
    G = Digraph(4)
    G.add_edge(0,3)
    G.add_edge(3,2)

    dfs = DirectedDepthFirstSearch(G, 0)

    print(dfs.marked(0)) # True
    print(dfs.marked(1)) # False
    print(dfs.marked(2)) # True
    print(dfs.marked(3)) # True

    print(dfs.count()) # 3
