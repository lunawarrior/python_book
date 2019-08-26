'''
This is the secod exercise in chapter 7

Write a function to sum all of the even numbers in a list.
Remember the definition of an even number.  When divided by 2, the remainder should be 0
'''
from test import test

#Define your sum_even function here
def sum_even(the_list):
    total = 0
    for item in the_list:
        if item % 2 == 0:
            total = total + item
    return total




# Here are the tests
test(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
test(sum_even([1, -1, 1, 1]), 0)
test(sum_even([3, 4, -6, 8]), 6)