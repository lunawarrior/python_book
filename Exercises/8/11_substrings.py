'''

Write a function that counts how many times a substring occurs in a string

'''
from test import test







test(count("is", "Mississippi"), 2)
test(count("an", "banana"), 2)
test(count("ana", "banana"), 2)
test(count("nana", "banana"), 1)
test(count("nanan", "banana"), 0)
test(count("aaa", "aaaaaa"), 4)