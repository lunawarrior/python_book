'''

Write a function that reverses its string argument, and satisfies these tests:


'''
from test import test
def reverse(the_str):
    the_reserve_string = ""
    for letter in the_str:
        the_reserve_string = letter + the_reserve_string
        # print(the_reserve_string)

    return the_reserve_string
    










test(reverse("happy"), "yppah")
test(reverse("Python"), "nohtyP")
test(reverse("racecar"), "racecar")
test(reverse(""), "")
test(reverse("a"), "a")

