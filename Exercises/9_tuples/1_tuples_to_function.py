def my_function(classes):
    for i in classes:
        print(i)

subjects = ("math", "biology", ("chemistry", "science",), ("reading"))
my_function(subjects)

