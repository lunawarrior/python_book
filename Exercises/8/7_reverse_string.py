'''

Write a function that reverses its string argument, and satisfies these tests:


'''
from test import test

def reverse(the_string_start):
    the_reversed_string = ''
    for char in the_string_start:
        the_reversed_string = char + the_reversed_string
    return the_reversed_string







test(reverse("happy"), "yppah")
test(reverse("Python"), "nohtyP")
test(reverse("racecar"), "racecar")
test(reverse(""), "")
test(reverse("a"), "a")

