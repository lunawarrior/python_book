# Add a method reflect_x to Point which returns a new Point, 
# one which is the reflection of the point about the x-axis. 
# For example, Point(3, 5).reflect_x() is (-3, 5)
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


#Tests
my_point = Point(3, 5)

reflected = my_point.reflect_x()
test.test(reflected.x == -3)
test.test(reflected.y == 5)

my_point2 = Point(-5, 2)

reflected2 = my_point2.reflect_x()
test.test(reflected2.x == 5)
test.test(reflected2.y == 2)