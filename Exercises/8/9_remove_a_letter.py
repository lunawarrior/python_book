'''

Write a function that removes all occurrences of a given letter from a string

'''
from test import test

def remove_letter(letter, word):
    # character
    the_string = ''
    for char in word:
        if char != letter:
            the_string = the_string + char
    return the_string
        
    




test(remove_letter("p", "happy"), "hay")
test(remove_letter("a", "apple"), "pple")
test(remove_letter("a", "banana"), "bnn")
test(remove_letter("z", "banana"), "banana")
test(remove_letter("i", "Mississippi"), "Msssspp")
test(remove_letter("b", ""), "")
test(remove_letter("b", "b"), "")
test(remove_letter("b", "c"), "c")