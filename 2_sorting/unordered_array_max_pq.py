"""
 *  
 *  Priority queue implementation with an unsorted array.
 * 
 *  Limitations
 *  -----------
 *   - no array resizing
 *   - does not check for overflow or underflow.
 *
"""

class UnorderedArrayMaxPQ:

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
        self.pq[self.size] = key
        self.size += 1
    
    # deletes and returns the max element in PQ
    def del_max(self):
        max_index = 0;
        for i in range(1, self.size):
            if (self._less(max_index, i)):
                max_index = i
            
        self._exch(max_index, self.size-1);
        self.size -= 1
        return self.pq[self.size];
    
    # Helper functions.
    def _less(self, i, j):
        return self.pq[i] < self.pq[j];
    

    def  _exch(self, i, j):
        swap = self.pq[i];
        self.pq[i] = self.pq[j];
        self.pq[j] = swap;
    

pq = UnorderedArrayMaxPQ(10)
pq.insert("this")
pq.insert("is")
pq.insert("a")
pq.insert("test")
while not pq.isEmpty():
    print(pq.del_max())

   