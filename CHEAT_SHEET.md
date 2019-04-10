
## Hash Table
 A hash table uses a hash function to map keys to integer values. Worst case run time for operations O(n) if there are collisions, but we generally assume collisions are infrequent. Hash tables handle collisions with either separate chaining or linear probing. It requires O(n) space to use a hash table, where n is the number of elements added. One can implement a hash table with the following code hash_table = {} in Python.

| Function        | Description                                         | Run Time (Average Case) | Memory |
|-----------------|-----------------------------------------------------|-------------------------|--------|
| put(key, value) | Adds key-value pair to the table.                   | O(1)                    | O(1)   |
| get(key)        | Returns the value associated with key if it exists. | O(1)                    | O(1)   |


## Sorting
 User the following code to sort a list with Python in N log N time.
```
list_to_sort = [1,4,3,5,2]
list_to_sort.sort()
print(list_to_sort) # [1,2,3,4,5]
```

| Sorting Algorithm                                | Is Stable? | Average Runtime | Worst Case Runtime | Space  |
|--------------------------------------------------|------------|-----------------|--------------------|--------|
| Quick Sort                                       | No         | O(n log n)      | O(n^2)             | O(1)   |
| Merge Sort                                       | Yes        | O(n log n)      | O(n log n)         | O(n)   |
| Key Index Count (strings of fixed alphabet only) | No         | O(n)            | O(n)               | O(1)   |


## Binary Search Tree. 
The worst case for a BST happens when the BST becomes a linked a linked list. It requiest O(n) space for a BST of size N.

| Function        | Description                                            | Unbalanced Worst Case Runtime | Unbalanced Average Case Run Time | Balanced Worst Case Run Time |
|-----------------|--------------------------------------------------------|-------------------------------|----------------------------------|------------------------------|
| put(key, value) | Insets key-value pair to BST                           | O(n)                          | O(log n)                         | O(log n)                     |
| get(key)        | Returns value associated with key if exists in the BST | O(n)                          | O(log n)                         | O(log n)                     |
| remove(key)     | Removes key-value pair from BST if exists.             | O(n)                          | O(log n)                         | O(log n)                     |

## Stack.
Using a linked list with a pointer to the top of the stack. Get elements in last in first out (LIFO) format. Requires O(n) space.

| Function    | Description                                           | Worst Case Run Time |
|-------------|-------------------------------------------------------|---------------------|
| push(value) | Pushes value to the top of the stack                  | O(1)                |
| pop()       | Removes and returns the value at the top of the stack | O(1)                |


##Queue.
Using a linked list with pointers to the front and end of the queue. Gets elements in first in first out (FIFO) format. Requires O(n) space.

| Function       | Description                                              | Worst Case Run Time |
|----------------|----------------------------------------------------------|---------------------|
| enqueue(value) | Adds value to the end of the queue.                      | O(1)                |
| dequeue()      | Removes and returns the value at the front of the queue. | O(1)                |


## Heap.
  Allows O(log n) operations for insert and remove_max. Good for keeping track of the largest (or smallest) elements in a set. A heap uses helper functions sink and swim to maintain heap property which is that the children of a node are always smaller (or larger in a MinHeap) than the parent. Requires O(n) space.

| Function (assume MaxHeap) | Description                                            | Worst Case Run Time |
|---------------------------|--------------------------------------------------------|---------------------|
| insert(value)             | Adds value to the MaxHeap.                             | O(log n)            |
| remove_max()              | Removes and returns the max element from the MaxHeap.  | O(log n)            |


## Graph Algorithms. 
V = number of vertices, E = number of edges. Note that BFS and DFS can be applied to Binary Trees as they are a specific example of a graph. All of the graph functions rely on an overarching graph structure.

| Function Name                                                                      | Function Signature            | Description                                                                                                                                                                                                                                                                                                                                                                                | Worst Case Runtime | Space Complexity |
|------------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------------|
| Breadth First Search (BFS)                                                         | bfs(source, target)           | Keeps track of visited nodes with a set. Starts with a queue just containing the source. Then iteratively removes items from the queue while adding the neighbors of the current node that have not been visited. Returns True if the target is found, False otherwise.                                                                                                                    | O(V + E)             | O(V)             |
| Depth First Search (DFS)                                                           | dfs(source, target)           | Keeps track of visited nodes with a set. Starts with a stack just containing the source. Then iteratively removes items from the stack while adding the neighbors of the current node that have not been visited. Returns True if the target is found, False otherwise.                                                                                                                    | O(V + E)             | O(V)             |
| Kruskall's Algorithm to find Minimum Spanning Tree (MST) of an edge-weighted graph | kruskalls()                   | A greedy algorithm that takes the edges of least weight and adds them to the MST if it does not create a cycle. Uses a priority queue on edges ordered by weight to get log(E) runtime.                                                                                                                                                                                                    | O(E log E)           | O(E)             |
| Prim’s to find Minimum Spanning Tree (MST) of an edge-weighted graph               | prims()                       | A greedy algorithm that adds builds off a single vertex by adding the edge of least weight that could be added to this MST. Also uses a priority queue to get the edge of least weight.                                                                                                                                                                                                    | O(E log E)           | O(E)             |
| Djikstra's Shortest Path                                                           | shortest_path(source, target) | Dijkstra's algorithm initializing dist[s] to 0 and all other distTo[] entries to positive infinity. Then, it repeatedly relaxes and adds to the tree a non-tree vertex with the lowest distTo[] value, continuing until all vertices are on the tree or no non-tree vertex has a finite distTo[] value. Uses a priority queue on the set of vertices to determine next vertex to examine.  | O(E log V)         | O(V)             |






