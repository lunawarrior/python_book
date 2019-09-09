'''

Now rewrite the count_letters function (from exercise 3) so that instead of traversing the string, it repeatedly calls the find method, 
with the optional third parameter to locate new occurrences of the letter being counted.


'''
from test import test
def count_letters(string, letter, number = 0):
    count = 0
    print(string[number:])
    for char in string[number:]: 
        if char == letter:
            
            count += 1
    return count
        




test(count_letters('banana', 'a'), 3)
test(count_letters('banana', 'a', 2), 2)
test(count_letters('banana', 'n'), 2)
test(count_letters('pineapple', 'p'), 3)
test(count_letters('pineapple', 'p', 3), 2)
test(count_letters('pineapple', 'z'), 0)