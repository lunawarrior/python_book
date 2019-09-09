'''

Now rewrite the count_letters function (from exercise 3) so that instead of traversing the string, it repeatedly calls the find method, 
with the optional third parameter to locate new occurrences of the letter being counted.


'''
from test import test
def count_letters(the_word, the_letter, the_number = 0):
    fruit = the_word[the_number:] 
    count = 0
    for char in fruit:
        if char == the_letter:
            # count = count + 1
            count += 1
    return count






test(count_letters('banana', 'a'), 3)
test(count_letters('banana', 'a', 2), 2)
test(count_letters('banana', 'n'), 2)
test(count_letters('pineapple', 'p'), 3)
test(count_letters('pineapple', 'p', 3), 2)
test(count_letters('pineapple', 'z'), 0)