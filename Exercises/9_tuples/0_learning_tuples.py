
# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# # # print(julia)

# # (name, surname, b_year, movie, m_year, profession, b_place) = julia

# # print(name)

# test_tuple = ('abc', 'def', ('item 0', 'item 1'))

# # print(test_tuple)

# # print(test_tuple[0])
# # print(test_tuple[1])
# # print(test_tuple[2])
# # print(test_tuple[2][0])
# # print(test_tuple[2][0][1])

# # test_tuple[1] = 'something'
# # 
# # print(test_tuple[0:2])

# test_tuple2 = test_tuple[:2] + ( 'ghi', 'fourth')

# print(test_tuple2)
# print(test_tuple2[3])




def divide_with_remainder(numbers):
    result = numbers[0] // numbers[1]
    remainder = numbers[0] % numbers[1]
    return (result, remainder)

a, b = divide_with_remainder( (13, 2) )


print(a)
print(b)

d, e = divide_with_remainder(15, 4)
print(d)
print(e)


# #Swap a and b
# (b, a) = (a, b)



# student = ("Stewart", ("Math", "Biology", "calculus"), "a third item")

# classes = student[1]
# bio = classes[1]

# #Print biology from student
# print(student[1][1])
