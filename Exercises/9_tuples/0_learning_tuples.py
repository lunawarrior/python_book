julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# print(julia)

(name, surname, b_year, movie, m_year, profession, b_place) = julia

def divide_with_remainder(top, bottom):
    result = top // bottom
    remainder = top % bottom
    return (result, remainder)

a, b = divide_with_remainder(13, 2)
# print(a)
# print(b)

#Swap a and b
(b, a) = (a, b)



student = ("Stewart", ("Math", "Biology", "calculus"), "a third item")

classes = student[1]
bio = classes[1]

#Print biology from student
print(student[1][1])
