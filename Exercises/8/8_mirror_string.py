'''

Write a function that mirrors its argument

'''
from test import test
def reverse(the_str):
    the_reverse_string = ""
    for letter in the_str:
        the_reverse_string = letter + the_reverse_string
        # print(the_reserve_string)

    return the_reverse_string

def mirror(the_word):
    the_reverse_string = reverse(the_word)
    the_word = the_word + the_reverse_string

    return the_word







test(mirror("good"), "gooddoog")
test(mirror("Python"), "PythonnohtyP")
test(mirror(""), "")
test(mirror("a"), "aa")