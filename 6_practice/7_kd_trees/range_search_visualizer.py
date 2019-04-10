
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
    

        double x0 = 0.0, y0 = 0.0      # initial endpoint of rectangle
        double x1 = 0.0, y1 = 0.0      # current location of mouse
        boolean isDragging = False     # is the user dragging a rectangle

        # draw the points
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(.01)
        for p in brute.points():
            p.draw()

        while (True):
            stddraw.show(40)

            # user starts to drag a rectangle
            if (stddraw.mousePressed() and not isDragging):
                x0 = stddraw.mouseX()
                y0 = stddraw.mouseY()
                isDragging = True
                continue
            

            # user is dragging a rectangle
            else if (stddraw.mousePressed() and isDragging):
                x1 = stddraw.mouseX()
                y1 = stddraw.mouseY()
                continue
            

            # mouse no longer pressed
            else if (!stddraw.mousePressed() and isDragging);
                isDragging = False
            


            rect = Rectangle(min(x0, x1), min(y0, y1),
                                     max(x0, x1), max(y0, y1))
            # draw the points
            stddraw.clear()
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.setPenRadius(.01)
            for p in brute.points():
                p.draw()

            # draw the rectangle
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.setPenRadius()
            rect.draw()

            # draw the range search results for brute-force data structure in red
            stddraw.setPenRadius(.03)
            stddraw.setPenColor(stddraw.RED)
            for p in brute.range(rect):
                p.draw()

            # draw the range search results for kd-tree in blue
            stddraw.setPenRadius(.02)
            stddraw.setPenColor(stddraw.BLUE)
            for p in kdtree.range(rect):
                p.draw()

            stddraw.show(40)
        
    

