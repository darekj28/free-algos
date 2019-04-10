# 1.3 Bags Stacks and Queues

Several fundamental data types involve collections of objects. Specifically, the set of values is a collection of objects, and the operations revolve around adding, removing, or examining objects in the collection. In this section, we consider three such data types, known as the bag, the queue, and the stack. They differ in the specification of which object is to be removed or examined next.

__APIs.__ We define the APIs for bags, queues, and stacks. Beyond the basics, these APIs reflect two Java features: generics and iterable collections.

```
class Bag:
    # creates an empty bag
    def __init__(self):

    # adds an item to this bag
    def add(self, item):

    # Returns a boolean indicating if the bag is empty
    def isEmpty(self):

    # returns the number of items in the bag
    def size(self):
```

```
class Queue:
    # creates an empty Queue
    def __init__(self):

    # adds an item to the queue
    def enqueue(self, item):

    # removes and returns the least recently added item 
    def dequeue(self):

    # Returns a boolean indicating if the queue is empty
    def isEmpty(self):

    # returns the number of items in the queue
    def size(self):
```

```
class Stack:
    # creates an empty Stack
    def __init__(self):

    # adds an item to the stack
    def push(self, item):

    # removes and returns the most recently added item 
    def pop(self):

    # Returns a boolean indicating if the stack is empty
    def isEmpty(self):

    # returns the number of items in the stack
    def size(self):
```

- _Bags._ A bag is a collection where removing items is not supported—its purpose is to provide clients with the ability to collect items and then to iterate through the collected items.
- _FIFO queues._ A FIFO queue is a collection that is based on the first-in-first-out (FIFO) policy. The policy of doing tasks in the same order that they arrive is one that we encounter frequently in everyday life: from people waiting in line at a theater, to cars waiting in line at a toll booth, to tasks waiting to be serviced by an application on your computer.
- _Pushdown stack._ A pushdown stack is a collection that is based on the last-in-first-out (LIFO) policy. When you click a hyperlink, your browser displays the new page (and pushes onto a stack). You can keep clicking on hyperlinks to visit new pages, but you can always revisit the previous page by clicking the back button (popping it from the stack). 
-_Arithmetic expression evaluation._ [evaluate.py](evalutate.py) is a stack client that evaluates fully parenthesized arithmetic expressions. It uses Dijkstra's 2-stack algorithm:
    - Push operands onto the operand stack.
    - Push operators onto the operator stack.
    - Ignore left parentheses.
    - On encountering a right parenthesis, pop an operator, pop the requisite number of operands, and push onto the operand stack the result of applying that operator to those operands.
This code is a simple example of an _interpreter._

__Linked lists.__ A linked list is a recursive data structure that is either empty (null) or a reference to a node having a generic item and a reference to a linked list. To implement a linked list, we start with a nested class that defines the node abstraction

```
class Node:
    def __init__(self, item , next = None):
        self.item = item
        self.next = next
```


- _Building a linked list._ To build a linked list that contains the items to, be, and or, we create a Node for each item, set the item field in each of the nodes to the desired value, and set the next fields to build the linked list.

![linked-list](linked-list.png)

- _Insert at the beginning._ The easiest place to insert a new node in a linked list is at the beginning.


![linked-list-insert-front](linked-list-insert-front.png)

- _Remove from the beginning._ Removing the first node in a linked list is also easy.

![linked-list-remove-first](linked-list-remove-first.png)

- _Insert at the end._ To insert a node at the end of a linked list, we maintain a link to the last node in the list.

![linked-list-insert-end](linked-list-insert-end.png)

- _Traversal._ The following is the idiom for traversing the nodes in a linked list.
```
x = self._first
while x is not None:
    # process x.item
    x = x.next
```


__Linked-list implementations of collections.__

- _Linked list implementation of a stack._ [stack.py](stack.py) implements a generic stack using a linked list. It maintains the stack as a linked list, with the top of the stack at the beginning, referenced by an instance variable __first__. To __push()__ an item, we add it to the beginning of the list; to __pop()__ an item, we remove it from the beginning of the list.
- _Linked list implementation of a queue._ Program [queue.py](queue.py) implements a generic FIFO queue using a linked list. It maintains the queue as a linked list in order from least recently to most recently added items, with the beginning of the queue referenced by an instance variable __first__ and the end of the queue referenced by an instance variable __last__. To __enqueue()__ an item, we add it to the end of the list; to __dequeue()__ an item, we remove it from the beginning of the list.
- _Linked list implementation of a bag_. Program [bag.py](bag.py) implements a generic bag using a linked list. The implementation is the same as [stack.py](stack.py) except for changing the name of __push()__ to __add()__ and removing __pop()__.

Iteration. To consider the task of implementing iteration, we start with a snippet of client code that prints all of the items in a collection of strings, one per line:

```
stack = Stack()
...
for s in stack.items():
    print(s)
...
```

## Review Exercises

1. Suppose that an intermixed sequence of (stack) push and pop operations are performed. The pushes push the integers 0 through 9 in order; the pops print out the return value. Which of the following sequence(s) could not occur?
```
(a)  4 3 2 1 0 9 8 7 6 5
(b)  4 6 8 7 5 3 2 9 0 1
(c)  2 5 6 7 4 8 9 3 1 0
(d)  4 3 2 1 0 5 6 7 8 9
(e)  1 2 3 4 5 6 9 8 7 0
(f)  0 4 6 5 3 8 1 7 2 9
(g)  1 4 7 9 8 6 5 3 0 2
(h)  2 1 4 3 6 5 8 7 9 0
```
2. Suppose that a client performs an intermixed sequence of (queue) enqueue and dequeue operations. The enqueue operations put the integers 0 through 9 in order onto the queue; the dequeue operations print out the return value. Which of the following sequence(s) could not occur?

```
(a)  0 1 2 3 4 5 6 7 8 9
(b)  4 6 8 7 5 3 2 9 0 1 
(c)  2 5 6 7 4 8 9 3 1 0
(d)  4 3 2 1 0 5 6 7 8 9
```

3. __Delete i<sup>th</sup> element.__ Create a data type that supports the following operations: isEmpty, insert, and remove(int i), where the deletion operation deletes and returns the ith least recently added object on the queue. Do it with an array, then do it with a linked list. What is the running time for each operation?

4. __Interview question.__ Given a stack of an unknown number of strings, print out the 5th to the last one. It's OK to destroy the stack in the process. Hint: use a queue of 5 elements.

5. __Palindrome checker.__ Write a program that reads in a sequence of strings and checks whether it constitutes a palindrome. Ignore punctuation and spaces and case. (A MAN, A PLAN, A CANAL - PANAMA). Use one stack and one queue.

6. __Streaming algorithm.__ Given a long sequence of items, design a data structure to store the _k_ items most recently seen.

