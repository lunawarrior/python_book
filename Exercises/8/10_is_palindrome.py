'''

Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):

'''
from test import test
def reverse(the_string_start):
    the_reversed_string = ''
    for char in the_string_start:
        the_reversed_string = char + the_reversed_string
    return the_reversed_string

def is_palindrome(word):
    the_reversed_string = reverse(word)
    # if the_reversed_string =
    if word == the_reversed_string:
        return True
    else:
        return False





test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))    # Is an empty string a palindrome?