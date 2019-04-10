# 4.1 Graphs



__Graphs.__ A _graph_ is a set of vertices and a collection of _edges_ that each connect a pair of vertices. We use the names 0 through V-1 for the vertices in a V-vertex graph.

![graph](graph.png)

__Glossary.__ Here are some definitions that we use.

- A _self-loop_ is an edge that connects a vertex to itself.
- Two edges are _parallel_ if they connect the same pair of vertices.
- When an edge connects two vertices, we say that the vertices are _adjacent_ to one another and that the edge is incident on both vertices.
- The _degree_ of a vertex is the number of edges incident on it.
- A _subgraph_ is a subset of a graph's edges (and associated vertices) that constitutes a graph.
- A _path_ in a graph is a sequence of vertices connected by edges. A _simple path_ is one with no repeated vertices.
- A _cycle_ is a path (with at least one edge) whose first and last vertices are the same. A _simple cycle_ is a cycle with no repeated edges or vertices (except the requisite repetition of the first and last vertices).
- The _length_ of a path or a cycle is its number of edges.
- We say that one vertex is _connected_ to another if there exists a path that contains both of them.
- A graph is _connected_ if there is a path from every vertex to every other vertex.
- A graph that is not connected consists of a set of _connected components_, which are maximal connected subgraphs.
- An _acyclic graph_ is a graph with no cycles.
- A _tree_ is an acyclic connected graph.
- A _forest_ is a disjoint set of trees.
- A _spanning tree_ of a connected graph is a subgraph that contains all of that graph's vertices and is a single tree. A _spanning forest_ of a graph is the union of the spanning trees of its connected components.
- A _bipartite graph_ is a graph whose vertices we can divide into two sets such that all edges connect a vertex in one set with a vertex in the other set.


![tree](tree.png)

__Undirected graph data type.__ We implement the following undirected graph API.

```
class Graph:
    # create a graph with V number of vertices and no edges
    def __init__(self, V): 

    # returns the number of vertices in this graph
    def V(self):

    # returns the number of edges in this graph
    def E(self):

    # add edge between u-v in this graph, u,v are vertices
    def add_edge(self, u, v):

    # returns all the neighbors of vertex v
    def adj(self, v):
```

The key method __adj()___ allows client code to iterate through the vertices adjacent to a given vertex. Remarkably, we can build all of the algorithms that we consider in this section on the basic abstraction embodied in __adj()__.

__Graph representation.__ We use the _adjacency-lists_ representation, where we maintain a vertex-indexed array of lists of the vertices connected by an edge to each vertex.

![adjacency-lists.png](adjacency-lists.png)

[graph.py](graph.py) implements the graph API using the adjacency-lists representation. [adj_matrix_graph.py](adj_matrix_graph.py) implements the same API using the adjacency-matrix representation.

__Depth-first search (DFS).__ Depth-first search is a classic recursive method for systematically examining each of the vertices and edges in a graph. To visit a vertex
- Mark it as having been visited.
- Visit (recursively) all the vertices that are adjacent to it and that have not yet been marked. 

[dfs.py](dfs.py) implements the depth first search approach to following API:

```
class Search:
    # find vertices in graph G connected to vertex s (source)
    def __init__(self, G, s): 

    # returns True if v is connected to s and False otherwise
    def marked(self, v):

    # returns number of vertices connected to s
    def count(self):
```

__Finding paths.__ It is easy to modify depth-first search to not only determine whether there exists a path between two given vertices but to find such a path (if one exists). We seek to implement the following API:

```
class Paths:
    # find paths in graph G from given vertex s (source)
    def __init__(self, G, s):

    # is there a path from source to v
    def has_path_to(self, v):

    # returns path from s to v if exists; returns null otherwise
    def path_to(self, v):
```


To accomplish this, we remember the edge __v-w__ that takes us to each vertex __w__ for the first time by setting __edgeTo[w]__ to __v__. In other words, __v-w__ is the last edge on the known path from __s__ to __w__. The result of the search is a tree rooted at the source; __edgeTo[]__ is a parent-link representation of that tree. [dfs_paths.py](dfs_paths.py) implements this approach.

__Breadth-first search.__ Depth-first search finds some path from a source vertex __s__ to a target vertex __v__. We are often interested in finding the _shortest_ such path (one with a minimal number of edges). Breadth-first search is a classic method based on this goal. To find a shortest path from __s__ to __v__, we start at __s__ and check for __v__ among all the vertices that we can reach by following one edge, then we check for v among all the vertices that we can reach from __s__ by following two edges, and so forth.

To implement this strategy, we maintain a queue of all vertices that have been marked but whose adjacency lists have not been checked. We put the source vertex on the queue, then perform the following steps until the queue is empty:

- Remove the next vertex __v__ from the queue.
- Put onto the queue all unmarked vertices that are adjacent to __v__ and mark them.

[bfs_paths.py](bfs_paths.py) is an implementation of the Paths API that finds shortest paths. 

__Connected components.__ Our next direct application of depth-first search is to find the connected components of a graph. Recall from Section 1.5 that "is connected to" is an equivalence relation that divides the vertices into equivalence classes (the connected components). For this task, we define the following API:

```
class CC:
    # contructor takes in a graph G
    def __init__(self, G):

    #  returns a boolean indicating if v, w are connected
    def connected(self, v, w):

    # returns the number of connected components
    def count(self):

    # component identifier for v
    def id(self, v)
```

[cc.py](cc.py) uses DFS to implement this API.

__Proposition.__ DFS marks all the vertices connected to a given source in time proportional to the sum of their degrees and provides clients with a path from a given source to any marked vertex in time proportional to its length.

__Proposition.__ For any vertex __v__ reachable from __s__, BFS computes a shortest path from __s__ to __v__ (no path from __s__ to __v__ has fewer edges). BFS takes time proportional to __V + E__ in the worst case.

__Proposition.__ DFS uses preprocessing time and space proportional to __V + E__ to support constant-time connectivity queries in a graph.

__More depth-first search applications.__ The problems that we have solved with DFS are fundamental. Depth-first search can also be used to solve the following problems:

- _Cycle detection:_ Is a given graph acyclic? One can use depth-first search to determine whether a graph has a cycle, and if so return one. It takes time proportional to __V + E__ in the worst case.
- _Two-colorability:_ Can the vertices of a given graph be assigned one of two colors in such a way that no edge connects vertices of the same color? One can use depth-first search to determine whether a graph has a bipartition; if so, return one; if not, return an odd-length cycle. It takes time proportional to V + E in the worst case.
- _Bridge:_ A _bridge_ (or cut-edge) is an edge whose deletion increases the number of connected components. Equivalently, an edge is a bridge if and only if it is not contained in any cycle. One can use depth-first search to find time the bridges in a graph. It takes time proportional to V + E in the worst case.
- _Biconnectivity:_ An _articulation vertex_ (or cut vertex) is a vertex whose removal increases the number of connected components. A graph is _biconnected_ if it has no articulation vertices. One can use depth-first search to find the bridges and articulation vertices. It takes time proportional to V + E in the worst case.
- _Planarity:_ A graph is _planar_ if it can be drawn in the plane such that no edges cross one another. The Hopcroft-Tarjan algorithm is an advanced application of depth-first search that determines whether a graph is planar in linear time.

# Review Exercises

1. Suppose you use a stack instead of a queue when running breadth-first search. Does it still compute shortest paths?
2. Write a program that performs depth-first-search iteratively (without recursion).
3. Write a program if a graph has non-trivial cycle, namely one with length at least 3.
4. __Delete a vertex without disconnecting a graph.__ Given a connected graph, design a linear-time algorithm to find a vertex whose removal (deleting the vertex and all incident edges) does not disconnect the graph.
