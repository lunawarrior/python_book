'''
If it is divisible by 3, print "Fizz"
if it is divisible by 5, print "Buzz"
if it is divisible by both, print "FizzBuzz"
otherwise print the number
'''
for i in range(1,11):
    if i % 3 == 0:
        print("Fizz")
    if i % 3 != 0:
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)