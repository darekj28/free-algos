import sys
from instream import InStream
from directed_bfs_paths import DirectedBreadthFirstPaths
from digraph_edge_list import Digraph

class SAP:
	# constructor takes a digraph (not necessarily a DAG)
	def __init__(self, G):

	# length of shortest ancestral path between v and w -1 if no such path
	def length(self, v, w):


	# a common ancestor of v and w that participates in a shortest ancestral path -1 if no such path. v and w are vertices.
	def ancestor(self, v,  w):


	# length of shortest ancestral path between any vertex in v and any vertex in w -1 if no such path. v_list, w_list are lists of vertices.
	def length_list(self, v_list, w_list):

	# a common ancestor that participates in shortest ancestral path -1 if no such path. v_list, w_list are lists of vertices.
	def ancestor_list(self, v_list, w_list):


if __name__ == "__main__":
    # build digraph from input file
    file_input = InStream(sys.argv[1])
    N = file_input.readInt()
    G = Digraph(N)
    E = file_input.readInt()
    while not file_input.isEmpty():
    	source = file_input.readInt()
    	target = file_input.readInt()
    	G.add_edge(source, target)

    # create a new SAP object
    test = SAP(G)
    # read in and print vertices the test starts from
    vertex1 = int(sys.argv[2])
    vertex2 = int(sys.argv[3])
    print("v = " + str(vertex1) + " w = " + str(vertex2))
    # test lenth and ancestor methods of SAP
    print("length = " + str(test.length(vertex1, vertex2)) + ", "
                           + "ancestor = " + str(test.ancestor(vertex1, vertex2)))