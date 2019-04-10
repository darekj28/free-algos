# Min Priority Queue (Heap)

## Description
Implement a Minimum Priority Queue in Python using a heap implementation that satisfies the following API such that it passes all of the unit tests. Ensure that all methods take `O(log n )` runtime in the worst-case.

```
# Implement a minimum heap with the array implementation. 
# The height of the element at the heap is determined by the index in the list.

class MinHeap:
    # Initializes an empty heap
    def __init__(self):
        
    # returns the size of the heap
    def size(self):
        
    # This helper function is to assist in the insert method
    # it is intended to swim a node up the heap until it 
    # is in the correct position. Here i represents the index in the list
    def _swim(self,i):

    # This helper function is to assist in the del_min method
    # it is intended to sink a node into the correct position in the heap
    # Here i represents the index in the list of the element you are sinking
    def _sink(self,i):

    # Inserts element k into the heap, while maintaining the heap property
    def insert(self,k):

    # Deletes the minimum element (the root) 
    # from the heap and returns that minimum element.
    def del_min(self):
```

## Testing
To check your code simply run 

```
python test_min_heap.py
```