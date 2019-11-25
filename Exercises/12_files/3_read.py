f = open("test.txt")
content = f.read()
f.close()

# print(content)

words = content.split()
print("There are {0} words in the file.".format(len(words)))

