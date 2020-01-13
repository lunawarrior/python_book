import turtle
win = turtle.Screen()

def make_crosshairs():
    crosshairs = turtle.Turtle()
    crosshairs.speed(0)
    crosshairs.backward(1000)
    crosshairs.forward(2000)
    crosshairs.backward(1000)
    crosshairs.left(90)
    crosshairs.backward(1000)
    crosshairs.forward(2000)

make_crosshairs()

def make_dot(x, y):
    my_turtle = turtle.Turtle()
    my_turtle.shape("circle")
    my_turtle.shapesize(.2, .2, .2)
    my_turtle.penup()
    xpos = x * 10
    ypos = y * 10
    my_turtle.setpos(xpos, ypos)


make_dot(5, 3)
win.mainloop()