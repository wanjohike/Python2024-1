# h_letters = []
# for letter in 'human':
#     h_letters.append(letter)
# print(h_letters)

# List comprehension
h_letters = [letter for letter in 'human']
print(h_letters)

# we can achieve the same result using a lamda expression
# with maps
letter = list(map(lambda x: x, 'human'))
print(letter)

# list comprehension allow you to creaate a new list by iterating over an erxiting iteration
# an applying a condition or transformation
# syntax = [exprestion for item in iterable if condition]

# create a list of square numbers from 1-5
square_nums = [x**2  for x in range(1 , 6)]
print(square_nums)

# create a list of even numbers from an existing list
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [x for x in numbers if x % 2 == 0]

# convert the following list comprehension
fruits = ['Mangos', 'Orange', 'Pineapples', 'Lemos', 'Mandizi', 'Mananasi']
new_fruits = []
for n in fruits:
    new_fruits.append(n)

print(new_fruits)


newfruitsComprehension = [n for n in fruits]
print(newfruitsComprehension)

# create a new list for fruits that start with M
m_fruit = [n for n in fruits if n.startswith('M')]
print(m_fruit)