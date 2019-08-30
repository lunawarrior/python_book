'''

Write a function that removes all occurrences of a given letter from a string

'''
from test import test







test(remove_letter("a", "apple"), "pple")
test(remove_letter("a", "banana"), "bnn")
test(remove_letter("z", "banana"), "banana")
test(remove_letter("i", "Mississippi"), "Msssspp")
test(remove_letter("b", ""), "")
test(remove_letter("b", "b"), "")
test(remove_letter("b", "c"), "c")