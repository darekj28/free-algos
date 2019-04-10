# Stack

## Description
Implement a Stack in Python that satisfies the following API such that it passes all of the unit tests. Ensure that all methods take `O(1)` runtime.

```
# Use this Node class to implement stack
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Stack:
    # Initializes an empty stack
    def __init__(self):

    # returns True if the stack is empty 
    # and False otherwise
    def isEmpty(self):

    # returns the number of elements in the stack
    def size(self):

    # pushes a value onto the stack
    # return value: void
    def push(self, value):

    # pops the top value off of the stack
    # and returns that item. 
    # If the stack is full simply return None and do nothing
    def pop(self):

    # returns the item at the top of the stack
    # but does not modify the stack
    def peek(self):
```

## Testing
To check your code simply run 

```
python test_stack.py
```