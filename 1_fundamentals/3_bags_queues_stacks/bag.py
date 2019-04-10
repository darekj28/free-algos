
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None



class Bag:
    # creates an empty bag
    def __init__(self):
        self._n = 0
        self._first = None

    # adds an item to this bag
    def add(self, item):
        old_first = self._first
        self._first = Node(item)
        self._first.next = old_first
        self._n += 1


    # Returns a boolean indicating if the bag is empty
    def isEmpty(self):
        return self.size() == 0

    # returns the number of items in the bag
    def size(self):
        return self._n 

    # returns a list of items in the bag.
    def items(self):
        output = []
        x = self._first
        while x is not None:
            output.append(x.item)
            x = x.next
        return output



if __name__ == "__main__":
    bag = Bag()
    for i in range(0, 5)[::-1]:
        bag.add(i)

    for item in bag.items():
        print(item)
    # prints : 0,1,2,3,4
