# 4. Graphs

__Overview.__ Pairwise connections between items play a critical role in a vast array of computational applications. The relationships implied by these connections lead to a host of natural questions: Is there a way to connect one item to another by following the connections? How many other items are connected to a given item? What is the shortest chain of connections between this item and this other item? 

We progress through the four most important types of graph models: undirected graphs (with simple connections), digraphs graphs (where the direction of each connection is significant), edge-weighted graphs (where each connection has an software associated weight), and edge-weighted digraphs (where each connection has both a direction and a weight).

- [4.1 Undirected Graphs](1_undirected_graphs) introduces the graph data type, including depth-first search and breadth-first search.
- [4.2 Directed Graphs](2_directed_graphs) introduces the digraph data type, including topological sort and strong components.
- [4.3 Minimum Spanning Trees](3_minimum_spanning_trees) describes the minimum spanning tree problem and two classic algorithms for solving it: Prim and Kruskal.
- [4.4 Shortest Paths](4_shortest_paths) introduces the shortest path problem and two classic algorithms for solving it: Dijkstra's algorithm and Bellman-Ford.