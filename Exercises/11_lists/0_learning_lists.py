# # Items in Lists
# students = [
#     ("John", ["CompSci", "Physics"]),
#     ("Vusi", ["Maths", "CompSci", "Stats"]),
#     ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
#     ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
#     ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# # Count how many students are taking CompSci
# counter = 0
# for (name, subjects) in students:
#     if "CompSci" in subjects:
#            counter += 1
#         #  counter = counter + 1

# print("The number of students taking CompSci is", counter)

# # concatenation
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# # Slices
# c = [0, 1, 2, 3, 4, 5, 6]
# print( c[3:5] )

# #Lists are mutable
# fruit = ["banana", "apple", "quince"]
# # print(fruit[1])
# fruit[1] = "strawaberry"
# print(fruit)

# # You can replace slices in a list
# a_list = ["a", "b", "c", "d", "e", "f"]
# # print(a_list[1:3])
# a_list[1:3] = ["x", "y"]
# print(a_list)

# # And remove them
# a_list[1:3] = []
# print(a_list)

# # And add them
# a_list[1:1] = ["b", "c"]
# print(a_list)


#11.9 Objects and references
# # a = "banana"
# # b = "banana"
# # print(a is b)

# a = [1, 2, 3] 
# b = [1, 2, 3]
# # # print( a == b )
# # # print( a is b )

# a[1] = 5
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a

# # print( a == b )
# # print( a is b )
# # print(a)
# # print(b)

# a[1] = 5
# print(a)
# print(b)

# # 11.11: Cloning lists
# a = [1, 2, 3]
# b = a[:]

# a[1] = 5
# print(a)
# print(b)


# lists and for loops
# friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# for friend in friends:
#     print(friend)

# for i in range(20):
#     print(i)

# for fruit in ["banana", "apple", "quince"]:
#     print("I like to eat " + fruit + "s!")

# for number in range(20):
#     if number % 3 == 0:
#         print(number)

xs = [1, 2, 3, 4, 5]

# for i in range(len(xs)):
#     xs[i] = xs[i]**2

# print(xs)

for i in xs:
    if i % 2 == 0:
        xs.append(i+1)
    print(i)


