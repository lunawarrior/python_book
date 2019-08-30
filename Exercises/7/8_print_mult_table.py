'''
This is the eighth exercise in chapter 7

Trace the execution of the last version of print_mult_table and figure out how it works.

There are no tests, examine the code and figure out how it works.  The debuger may be useful. 

Homework, modify this to take two inputs, one for how wide it is and one for how tall it is
'''

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="   ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, high)

#Call print_mult_table with various numbers, for example
#print_mult_table(5)
print_mult_table(15)