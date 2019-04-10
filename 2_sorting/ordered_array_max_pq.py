

class OrderedArrayMaxPQ:

    # set inititial size of heap to hold size elements
    def __init__(self, capacity):
        self.capacity = capacity # capacity of the PQ
        self.pq = [0] * capacity # array of elements in PQ
        self.size = 0; # number of elements in PQ
    
    # is PQ empty?
    def isEmpty(self):
        return self.size == 0

    # returns size of PQ
    def size(self):
        return self.size
    
    # inserts key into PQ
    def insert(self, key):
        if self.size >= self.capacity:
            print("over capacity, nothing will happen")
            return 
        i = self.size - 1
        while i >= 0 and self._less(key, self.pq[i]):
            self.pq[i+1] = self.pq[i]
            i -= 1
        self.pq[i+1] = key
        self.size += 1
    
    # deletes and returns the max element in PQ
    def del_max(self):
        self.size -= 1
        return self.pq[self.size]
    
    # Helper functions.
    def _less(self, x, y):
        return x < y;
    

    

pq = OrderedArrayMaxPQ(10)
pq.insert("this")
pq.insert("is")
pq.insert("a")
pq.insert("test")
while not pq.isEmpty():
    print(pq.del_max()) # this test is a


