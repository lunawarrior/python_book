
'''
This is the first exercise in chapter 6:

The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”. 
Write a function turn_clockwise that takes one of these four compass points as its parameter, 
and returns the next compass point in the clockwise direction. Here are some tests that should pass:
'''
from test import test

# Define your turn_clockiwse function here
def turn_clockwise(direction):
    if(direction == "N"):
        return "E"
    elif(direction == "E"):
        return "S"
    elif(direction == "S"):
        return "W"
    else:
        return "N"
# Here are the tests
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise("E") == "S")

''' When you have those working, other values should return None.  Uncomment the below tests '''
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)