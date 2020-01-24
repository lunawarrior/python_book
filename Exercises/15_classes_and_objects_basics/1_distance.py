from point import Point

#Rewrite the distance function so that it takes two instances of the Point class rather than 4 ints

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result
def distance(new_point, last_point):
    dx = new_point.x - last_point.x
    dy = new_point.y - last_point.y
    return ((dx ** 2) + (dy ** 2)) ** .5

    

p = Point(5, 5)
p2 = Point(2, 1)

print(distance(p, p2))


# print(distance(5, 5, 2, 1))