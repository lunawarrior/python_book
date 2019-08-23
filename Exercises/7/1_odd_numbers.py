'''
This is the first exercise in chapter 7

Write a function to count how many odd numbers are in a list.
Remember the definition of an odd number.  When divided by 2, the remainder should be 1
'''
from test import test

#Define your count_odd function here
def count_odd(the_list):
    count = 0
    #Step through every item in the list
    for item in the_list:
        #identify odd numbers
        if item % 2 == 1:
            count = count + 1
        #if odd, add one to a variable

    #return the variable
    return count

# Here are the tests
test(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
test(count_odd([1, -1, 1, 1]), 4)
test(count_odd([2, 4, -6, 8]), 0)


