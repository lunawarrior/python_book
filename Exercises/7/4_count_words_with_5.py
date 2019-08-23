'''
This is the fourth exercise in chapter 7

Write a function to count how many words in a list have length 5.
'''
from test import test

#Define your count_5 function here
def count_5(the_list):
    count = 0
    for item in the_list:
        if (len(item)) == 5:
            count = count + 1
    
        print (len(item))
    return count
    
    
    



# Here are the tests
test(count_5(['a', 'word', 'abcde', 'exact', 'five']), 2)
test(count_5(['a', 'word', 'abcde', 'exact', 'five', 'thisa', 'hijlk']), 4)
