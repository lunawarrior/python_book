import turtle
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
    
    def make_dot(self, my_turtle = None):
        if my_turtle == None:
            my_turtle = turtle.Turtle()
            my_turtle.shape("circle")
            my_turtle.shapesize(.2, .2)
            my_turtle.penup()
        xpos = self.x * 10
        ypos = self.y * 10
        my_turtle.setpos(xpos, ypos)

    def make_dot(self, my_turtle = None):
        if my_turtle == None:
            my_turtle = turtle.Turtle()
            my_turtle.shape("circle")
            my_turtle.shapesize(.2, .2)
            my_turtle.penup()
        xpos = self.x * 10
        ypos = self.y * 10
        my_turtle.setpos(xpos, ypos)

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)
    
def make_crosshairs():
    crosshairs = turtle.Turtle()
    crosshairs.speed(0)
    crosshairs.backward(1000)
    crosshairs.forward(2000)
    crosshairs.backward(1000)
    crosshairs.left(90)
    crosshairs.backward(1000)
    crosshairs.forward(2000)

def make_crosshairs():
    crosshairs = turtle.Turtle()
    crosshairs.speed(0)
    crosshairs.backward(1000)
    crosshairs.forward(2000)
    crosshairs.backward(1000)
    crosshairs.left(90)
    crosshairs.backward(1000)
    crosshairs.forward(2000)

if __name__ == '__main__':
    p = Point(3, 5)         # Instantiate an object of type Point
    p2 = Point()
    p3 = Point(10, 10)

    half = p.halfway(p2)

    p.make_dot()
    p2.make_dot()
    p3.make_dot()

    print("p:  (x={0}, y={1})".format(p.x, p.y))
    print("p:  {0}".format(p))
    print("p2: (x={0}, y={1})".format(p2.x, p2.y))
    print("half: {}".format(half))
    print(p.distance_from_origin())
    
    make_crosshairs()
    win = turtle.Screen()
    win.mainloop()
