#Test Driven Development, write the tests, then write the code that will pass those tests.
# We’d like to know the index where a specific item occurs within in a list of items. 
# Specifically, we’ll return the index of the item if it is found, or we’ll return -1 if 
# the item doesn’t occur in the list.

# I have written some tests below, write a search_linear that will pass them.
#   I would suggest using a "for" loop, "enumerate", and an "if" statement

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

def search_linear(a_list,item):
    for (i,val) in enumerate(a_list):
        if (val == item ):
            print('Found it!')
            return i
    return -1
        





from test import test
test(search_linear(friends, "Zoe") == 1)
test(search_linear(friends, "Joe") == 0)
test(search_linear(friends, "Paris") == 6)
test(search_linear(friends, "Bill") == -1)


# Talk about Linear time