# Binary Search Tree (BST)

## Description
Implement a Binary Search Tree in Python that satisfies the following API such that it passes all of the unit tests. Ensure that all of the methods take `O(log n)` with the exception of the iterator.

```
# You will want to use the following Node class to write your BST
def Node:
    def init(self, value = None):
        self.value = value
        self.left = None
        self.right = None

def BST:
    # initializes an empty BST
    def init(self):

    # inserts the given value into the BST
    def put(self, value):

    # Return true if BST contains the value
    # returns false otherwise
    def contains(self, value):

    # deletes the given value from the BST if it exists, 
    # returns that value if it exists. Returns null if the value does not exist
    def delete(self, value):

    # returns the size of this BST
    def size(self):

    # returns true if the BST is empty, false otherwise
    def is_empty(self):

    # returns an iterator for all values in this BST in order
    def iterator(self):
```

## Testing
To check your code simply run 

```
python test_bst.py
```