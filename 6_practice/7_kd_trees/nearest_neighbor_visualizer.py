
import sys
from instream import InStream
from point import Point
from rectangle import Rectangle
from kdtree import KdTree
from point_set import PointSet


if __name__ == "__main__":
    filename = sys.argv[1]
    in_file = InStream(filename)
    stddraw.show(0)

    # initialize the two data structures with point from standard input
    brute = PointSet()
    kdtree = KdTree()
    i = 0
    while  not in_file.isEmpty():
        double x = in_file.readDouble()
        double y = in_file.readDouble()
        p = Point(x, y)
        kdtree.put(p, i)
        brute.put(p, i)
        i += 1
    

    while True:

        # the location (x, y) of the mouse
        double x = stddraw.mouseX()
        double y = stddraw.mouseY()
        query = Point(x, y)

        # draw all of the points
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(.01)
        for p in brute.points():
            p.draw()

        # draw in red the nearest neighbor according to the brute-force algorithm
        stddraw.setPenRadius(.03)
        stddraw.setPenColor(stddraw.RED)
        brute.nearest(query).draw()
        stddraw.setPenRadius(.02)

        # draw in blue the nearest neighbor according to the kd-tree algorithm
        stddraw.setPenColor(stddraw.BLUE)
        kdtree.nearest(query).draw()
        stddraw.show(0)
        stddraw.show(40)
    


