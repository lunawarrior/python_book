'''

Write a function that mirrors its argument

'''
from test import test

def reverse(the_string_start):
    the_reversed_string = ''
    for char in the_string_start:
        the_reversed_string = char + the_reversed_string
    return the_reversed_string

def mirror(the_string):
    mirror_string = reverse(the_string)
    mirror_string = the_string + mirror_string
    return mirror_string





test(mirror("good"), "gooddoog")
test(mirror("Python"), "PythonnohtyP")
test(mirror(""), "")
test(mirror("a"), "aa")