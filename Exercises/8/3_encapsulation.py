'''
This is the third exercise in chapter 8

Encapsulate the following code (lines 16-21) in a function named count_letters.

generalize it so that it accepts the string and the letter as arguments. 
Make the function return the number of characters, rather than print the answer. The caller should do the printing.

I would suggest refreshing yourself on string functions here:
http://openbookproject.net/thinkcs/python/english3e/strings.html#summary

'''
from test import test



# fruit = "banana"
# count = 0
# for char in fruit:
#     if char == "a":
#         count += 1
# print(count)

def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count
            


test(count_letters('banana', 'a'), 3)
test(count_letters('banana', 'n'), 2)
test(count_letters('pineapple', 'p'), 3)
test(count_letters('pineapple', 'z'), 0)