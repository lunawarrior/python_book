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
a = "banana"
b = "banana"
print(a is b)

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


# 11.12: lists and for loops

# # You can itterate through a list simply using a for loop
# friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# for friend in friends:
#     print(friend)

# # Lists are mutable, and you often want to traverse the list, changing each element.
# # The following code squares each element in the list xs
# xs = [1, 2, 3, 4, 5]

# for i in range(len(xs)):
#     xs[i] = xs[i]**2
# print(xs)


# # However range(len(xs)) is being used to get the index, 
# # but we want both the index and the value of the items in the list.
# # Python gives us a good way to do that using "enumerate":
# xs = [1, 2, 3, 4, 5]

# for (i, val) in enumerate(xs):
#     xs[i] = val**2
# print(xs)


# # enumerate gives both the index of an item, and its value during list traversal.
# # This example should be more clear as to how it works.
# for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
#     print(i, v)


# 11.13 List Parameters

# # Passing a list as a paramerter to a function actually passes a reference to the list,
# # Not a copy or clone.  Thus any changes the function makes to the list are also done 
# # to the list outside of that function.
# # For example, this function multiplies each element in the list given to it by 2.
# def double_stuff(a_list):
#     for (idx, val) in enumerate(a_list):
#         a_list[idx] = 2 * val

# things = [2, 5, 9]
# print(things)
# double_stuff(things)
# print(things)

# # 11.14 List Methods
# # Lists have several built-in methods, we will start with "append", which adds an item to the end.
# my_list = []
# my_list.append(5)
# my_list.append(15)
# my_list.append(27)
# my_list.append(3)
# print(my_list)


# # 11.15 Pure functions and modifiers
# # functions that change their arguments are called "modifiers", and the changes are called "side effects"
# # A "Pure function" does not produce any side effects.  It does not modify its parameters, and 
# # all changes are through the return function.
# # Here is double_stuff written as a pure function:
# def double_stuff(a_list):
#     new_list = []
#     for value in a_list:
#         new_elem = 2 * value
#         new_list.append(new_elem)
#     return new_list

# things = [2, 5, 9]
# other_things = double_stuff(things)
# print(things)
# print(other_things)

# 11.16 Functions that produce lists
# Interesting pattern shown above that can be used mos of the time when returning a list:

# initialize a result variable to be an empty list
# loop
#     create a new element
#     append it to result
# return the result


