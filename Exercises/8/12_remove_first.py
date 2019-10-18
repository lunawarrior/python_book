'''

Write a function that removes the first occurrence of a string from another string:

'''
from test import test


def remove(part,word):
    #print(word.find(part))
    #print(word.split('a'))
    index = word.find(part)
    #print(word[:index])

    #print(word[index + len(part):]
    print(index)
    if index > -1:
        return word[:index] + word[index + len(part):]
    else:
        return word
        


test(remove("an", "banana"), "bana")
test(remove("cyc", "bicycle"), "bile")
test(remove("iss", "Mississippi"), "Missippi")
test(remove("eggs", "bicycle"), "bicycle")