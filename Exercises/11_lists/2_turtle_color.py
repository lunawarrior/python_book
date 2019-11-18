# Consider this fragment of code
# Does this fragment create one or two turtle instances?
# Does setting the color of alex also change the color of tess? Explain in detail.

# You can test your hypothesis by uncommenting the commented lines below and running the code



import turtle

wn = turtle.Screen()        # Set up the window and its attributes

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
tess.color("green")

tess.forward(50)
tess.color('blue')
wn.mainloop()