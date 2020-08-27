'''
This is the second exercise in chapter 6:

Write a function day_name that converts an integer number 0 to 6 into the name of a day. 
Assume day 0 is “Sunday”. Once again, return None if the arguments to the function are not valid. 
Here are some tests that should pass:
'''
from test import test

# Define your day_name function here
def day_name(day):
    if day == 0:
        return "Sunday"
    elif(day == 1):
        return "Monday"
    elif(day == 2):
        return "Tuesday"
    elif(day == 3):
        return "Wednesday"
    elif(day == 4):
        return "Thursday"
    elif(day == 5):
        return "Friday"
    elif(day == 6):
        return "Saturday"

# Here are the tests
test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None)