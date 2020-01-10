# Add a method slope_from_origin which returns the slope of the line joining the origin to the point.
# For example "Point(4, 10).slope_from_origin()" sould return 2.5
# What cases will this method fail?
import test

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x = 0, y = 0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


test.test(Point(4,10).slope_from_origin(), 2.5)
test.test(Point(10,10).slope_from_origin(), 1)
test.test(Point(10,0).slope_from_origin(), 0)