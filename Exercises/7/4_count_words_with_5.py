'''
This is the fourth exercise in chapter 7

Write a function to count how many words in a list have length 5.
'''
from test import test

#Define your count_5 function here


# Here are the tests
test(count_5(['a', 'word', 'abcde', 'exact', 'five']) == 2)
test(count_5(['a', 'word', 'abcde', 'exact', 'five', 'thisa', 'hijlk']) == 4)
