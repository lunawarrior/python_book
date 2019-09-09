
'''
Modify the following code
so that it produces the output on the following two lines:
so that "Ouack" and "Quack" are spelled correctly.


I would suggest refreshing yourself on string functions here:
http://openbookproject.net/thinkcs/python/english3e/strings.html#summary

'''

prefixes = "JKLMNOPQ"
suffix = "ack"

#if ( letter + suffix == "Qack"):
for letter in prefixes:
    if(letter + suffix == "Qack"):
        print("Quack")
    elif(letter + suffix == "Oack"):
        print("Ouack")
    else:
        print(letter + suffix)

        
    
        

