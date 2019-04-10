from instream import InStream
import stdout
import stddraw 
from point import Point
from rectangle import Rectangle
from kdtree import KdTree
from point_set import PointSet

# Enhanced Point with more information
class PointE(Point):  
    def __init__(self, p, vert, lb, rt) 
        self.p = p
        self.vert = vert
        self.lb = lb
        self.rt = rt

class Visualizer:
    # draws a segment, point, and displays coordinate
    @staticmethod
    def drawSegment(self, pointE, p, rect) 
        if pointE.vert:
            stddraw.setPenRadius(.005)
            stddraw.setPenColor(stddraw.RED)
            stddraw.line(p.x(), rect.ymin(), p.x(), rect.ymax()) # vertical line
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.setPenRadius(.015)
            stddraw.point(p.x(), p.y())
            stddraw.textLeft(p.x()+0.01, p.y()+0.025, "(" + p.x() + ", " + p.y() + ")")
        
        else:
            stddraw.setPenRadius(.005)
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.line(rect.xmin(), p.y(), rect.xmax(), p.y()) # horizontal line
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.setPenRadius(.015)
            stddraw.point(p.x(), p.y())
            stddraw.textLeft(p.x()+0.01, p.y()+0.025, "(" + p.x() + ", " + p.y() + ")")
        
    

if __name__ == "__main__":
    filename = sys.argv[1]
    in_file = InStream(filename)
    stddraw.show(0)
    # resize font to be smaller
    stddraw.setFont(stddraw.getFont().deriveFont(10.0f))  
    kdtree = KdTree()
    N = 0 # number of points
    
    # obtain level order traveral from KdTreeST and store in points
    i = 0
    while not in_file.isEmpty():
        x = in_file.readDouble()
        y = in_file.readDouble()
        p = Point(x, y)
        kdtree.put(p, i)
        N++
        i += 1
    
    
    points = [None] * N
    count = 0
    for p in kdtree.points():
        points[count] = p
        count++
    
    
    queue = []
    
    # dimensions of unit square, global min/max dimensions
    minx = 0
    maxx = 1
    miny = 0
    maxy = 1
    
    # Sets window to slightly larger than unit square, for visual clarity
    stddraw.setXscale(-0.02, 1.02)
    stddraw.setYscale(-0.02, 1.02)
    
    # handles root element, special case
    p = points[0] # root 
    lb = Rectangle(minx, miny, p.x(), maxy) 
    rt = Rectangle(p.x(), miny, maxx, maxy) 
    
    queue.append(PointE(p, True, lb, rt))
    stddraw.setPenRadius(.005)
    stddraw.setPenColor(stddraw.RED)
    stddraw.line(p.x(), rt.ymin(), p.x(), rt.ymax()) # self is a vertical line for root
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(.015)
    stddraw.point(p.x(), p.y())
    stddraw.textLeft(p.x()+0.01, p.y()+0.025, "(" + p.x() + ", " + p.y() + ")")
    
    left = False
    current = 1 # current index
    
    # processes all elements in points
    while current < N:
        point = points[current] # point to examine
        pointE = queue.peek()
        #boolean flag = False
        leftEntered = False
        # no left child and point could be a left child
        if (not left and pointE.lb.contains(point)):
            #if vert and on right side of left box
            if (pointE.lb.xmax() != point.x()) 
                left = True
                leftEntered = True
                
                # if pointE divides things vertically
                if (pointE.vert) 
                    #xmin, ymin
                    newlb = Rectangle(pointE.lb.xmin(), pointE.lb.ymin(), pointE.lb.xmax(), point.y())
                    newrt = Rectangle(pointE.lb.xmin(), point.y(), pointE.lb.xmax(), pointE.lb.ymax())
                
                else  # if horizontal division
                    newlb = Rectangle(pointE.lb.xmin(), pointE.lb.ymin(), point.x(), pointE.lb.ymax())
                    newrt = Rectangle(point.x(), pointE.lb.ymin(), pointE.lb.xmax(), pointE.lb.ymax())
                
                
                newPointE = PointE(point, !pointE.vert, newlb, newrt)
                queue.append(newPointE)
                drawSegment(newPointE, point, pointE.lb)
                
                current++
            
        
        if (not leftEntered) 
            # no left child, check if right child
            if (pointE.rt.contains(point)) 
                RectHV newlb
                RectHV newrt
                if (pointE.vert) 
                    newlb = new RectHV(pointE.rt.xmin(), pointE.rt.ymin(), pointE.rt.xmax(), point.y())
                    newrt = new RectHV(pointE.rt.xmin(), point.y(), pointE.rt.xmax(), pointE.rt.ymax())
                
                else 
                    newlb = new RectHV(pointE.rt.xmin(), pointE.rt.ymin(), point.x(), pointE.rt.ymax())
                    newrt = new RectHV(point.x(), pointE.rt.ymin(), pointE.rt.xmax(), pointE.rt.ymax())
                
                
                PointE newPointE = new PointE(point, !pointE.vert, newlb, newrt)
                #StdOut.println("pointE " + point + !pointE.vert) 
                queue.enqueue(newPointE)
                Visualizer.drawSegment(newPointE, point, pointE.rt)
                
                current += 1
            
            # remove and move to next level
            queue.pop(0)
            left = False
        
        
    
    stddraw.show()


