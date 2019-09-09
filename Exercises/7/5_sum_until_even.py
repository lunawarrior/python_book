'''
This is the fifth exercise in chapter 7

Write a function to sum all of the numbers up to but not including the first even number in the list

Remember the definition of an even number.  When divided by 2, the remainder should be 0
I would suggest using a break
'''
from test import test

#Define your sum_until_even function here
def sum_until_even(the_list):
    sum = 0
    for item in the_list:
        if item % 2 == 0:
            break


        else:
            sum = sum + item
    return sum 
            
            


    


# Here are the tests
test(sum_until_even([1, 3, 3, 4, 5, 6, 7, 8, 9, 10]), 7)
test(sum_until_even([1, 5, 3, 1]), 10)
test(sum_until_even([3, -5, 6, 8]), -2)
