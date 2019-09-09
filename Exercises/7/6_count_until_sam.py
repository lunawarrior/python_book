'''
This is the sixth exercise in chapter 7

Count how many words occur in a list up to and including the first occurrence of the word “sam”.

I would suggest using a break
'''
from test import test

#Define your count_until_sam function here
def count_until_sam(the_list):
    count = 0
    for item in (the_list):
        if item == "sam":
            count = count + 1
            break
            
        
        else:
            count = count + 1
    return count
        



# Here are the tests
test(count_until_sam(['4', 'words', 'until', 'sam', 'and', 'some', 'after']), 4)
test(count_until_sam(['some', 'words', 'in', 'here', 'but', 'not', 'many', 'sam']), 8)
test(count_until_sam(['sam']), 1)
test(count_until_sam(['what', 'if', 'it', 'isn\'t', 'in', 'the', 'list?']), 7)


