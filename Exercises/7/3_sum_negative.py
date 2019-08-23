'''
This is the third exercise in chapter 7

Write a function to sum all of the negative numbers in a list.
'''
from test import test

#Define your sum_negative function here



# Here are the tests
test(sum_negative([1, -2, 3, 4, -5, 6, 7, -8, 9, 10]) == -15)
test(sum_negative([1, -1, 1, 1]) == -1)
test(sum_negative([3, 4, -6, -8]) == -14)