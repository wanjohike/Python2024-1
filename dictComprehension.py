# dict Comprehnsion allow you to create a new dictionary by iterating an exsiting 
# specfying key-value pairs
# syntax - '{key_expression: value_expression for item in iterable if condition}'

# create a dictionary of numbers range 1-5
square_nums = []

keys = ['a', 'b', 'c', 'd', 'e']
values = [1,2,3,4,5]

dictionary = {k: v for k, v in(zip(keys,values))}
print(dictionary)