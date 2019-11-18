# What is the Python interpreter’s response to the following?

# The three arguments to the range function are start, stop, and step, respectively. 
# In this example, start is greater than stop. (Like the commented line) What happens if start < stop and step < 0? 
# Write a rule for the relationships among start, stop, and step.



the_list = list(range(10, 0, -2))
# the_list = list(range(0, 10, 2))
print(the_list)
