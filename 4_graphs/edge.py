
class Edge:
    # initializes an edge between vertices v and w with a certain edge-weight
    def __init__(self, v, w, weight):
    	self._v = v
    	self._w = w
    	self._weight = weight

    # returns the weight of this edge
    def weight(self):
    	return self._weight

    # returns either vertex in this edge
    def either(self):
    	return self._v

    # returns the other vertex in this edge
    def other(self, v):
    	if v == self._v:
    		return self._w
    	else:
    		return self._v

    # compares to another edge's weight
    def __cmp__(self, other_edge):
    	return self.weight() > other_edge.weight()

    def __repr__(self):
    	return str((self._v, self._w, self._weight))