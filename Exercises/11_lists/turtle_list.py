import turtle             # Allows us to use turtles

alex = turtle.Turtle() 
wn = turtle.Screen()

colors = ['green', 'blue', 'yellow', 'red', 'black', 'teal', 'gray']

for i in colors[3::-1]:
    alex.color(i)
    alex.forward(50)
    alex.left(90)


wn.mainloop()

