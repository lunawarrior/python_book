
'''
This is the first exercise in chapter 6:

"The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”. 
Write a function turn_clockwise that takes one of these four compass points as its parameter, 
and returns the next compass point in the clockwise direction. Here are some tests that should pass:"
'''
from test import test

# Define your turn_clockiwse function here

test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
