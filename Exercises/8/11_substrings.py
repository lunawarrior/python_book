'''

Write a function that counts how many times a substring occurs in a string

'''
from test import test

def count(substring, the_string):
    count = 0
    for num in range(len(the_string)):
        # print(the_string[num:num+2])
        if (the_string[num:num+len(substring)] == substring):
            count = count + 1
    return count
    




test(count("is", "Mississippi"), 2)
test(count("an", "banana"), 2)
test(count("ana", "banana"), 2)
test(count("nana", "banana"), 1)
test(count("nanan", "banana"), 0)
test(count("aaa", "aaaaaa"), 4)