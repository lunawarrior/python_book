from point import Point

#Rewrite the distance function so that it takes two instances of the Point class rather than 4 ints

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

def distance(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

p= Point(3,5)
p2 = Point(6,1)
print(p.x)
print(p.y)
print(distance(p, p2))
