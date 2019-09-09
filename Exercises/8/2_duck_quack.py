
'''
Modify the following code
so that it produces the output on the following two lines:
so that "Ouack" and "Quack" are spelled correctly.


I would suggest refreshing yourself on string functions here:
http://openbookproject.net/thinkcs/python/english3e/strings.html#summary

'''

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'Q':
        print('Q' + "uack")
    elif letter == 'O':
        print('O' + 'uack')
    else:
        print(letter + suffix)
        
        

    

