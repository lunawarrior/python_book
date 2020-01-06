class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x = 0, y = 0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return ((self.x**2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return '({0}, {1})'.format(self.x,self.y)

p = Point() 
p.x = 5
p.y = 6
p2 = Point(2)

print("(x={0}, y = {1})".format(p.x, p.y))     
print("(x={0}, y = {1})".format(p2.x,p2.y)) 

print('p:  {0}'.format(p.distance_from_origin()))
print('p2:  {0}'.format(p2.distance_from_origin()))

print(p)


def print_point(pt):
    print('({0},{1})'.format(pt.x, pt.x))

q = Point()         # Make a second point



print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y