'''

Write a function that removes all occurrences of a string from another string:

'''
from test import test

def remove(part, word):

    index = word.find(part)
    # print(word[:index])

    # print(index)
    if index > -1:
        return word[:index] + word[index+len(part):]
    else:
        return word

def remove_all(part, word):
    while part in word:
        print(remove(part, word))
        word = remove(part, word)
    return word
        


test(remove_all("an", "banana"), "ba")
test(remove_all("cyc", "bicycle"), "bile")
test(remove_all("iss", "Mississippi"), "Mippi")
test(remove_all("eggs", "bicycle"), "bicycle")