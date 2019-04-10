# Deque

## Description
A double-ended queue or deque (pronounced "deck") is a generalization of a stack and a queue that supports inserting and removing items from either the front or the back  of the data structure. 

Create a generic data type Deque that implements the following API:

```
# Helper Node class
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    # initialize an empty deque
    def __init__(self):

    # is the deque empty?
    # returns a Boolean 
    def isEmpty(self):

    # returns the number of items in the deque
    def get_size(self):

    # inserts item to the front of the deque
    def addFirst(self, item):
    
    # inserts item at the end of the deque
    def addLast(self, item):

    # delete and return the item at the front of the deque 
    def removeFirst(self):

    # delete and return the item at the end of the deque
    def removeLast(self):
    
    # return an iterator over items in order from front to end (can be a list in Python)
    def iterator(self):

# main method , put unit tests here.
if __name__ == "__main__":
    pass

```

Your deque implementation should support each deque operation in 
constant worst-case time and use space proportional to the number 
of items currently in the deque.

Raise an exception if the client tries to remove an item from an empty Deque.

## Testing
To check your code simply run 

```
python test_deque.py
```