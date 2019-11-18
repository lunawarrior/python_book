from test import test
def add_vectors(a , b):
    to_return = []
    for i , j in zip(a , b):
        to_return.append(i + j)
        print(i)
        print(j)
        print('---')
    return to_return

    

# test(add_vectors([1, 1], [1, 1]), [2, 2])
# test(add_vectors([1, 2], [1, 4]), [2, 6])
test(add_vectors([1, 2, 3], [4, 5, 6]), [5, 7, 9])