# Create a list of 5 your favorite fruits
fav_fruit = ['bananas', 'mangoes', 'pineapples', 'passions', 'oranges']

# Add two more fruits to the list
add_fruit = ['strawberry', 'apple']
fav_fruit.extend(add_fruit)

# Remove the third fruit from the list
fav_fruit.pop(2)

# Print the final list and its length
print(fav_fruit)

# Create a dictionary with 3 key-value pairs representing a person's details(name, age, city).
person = {
    'Name' : 'Erick',
    'Age' : 23,
    'City' : 'Karatina'
}

# Add a new key-value pair for the person's occupation
person['Occupations'] = 'Kazi mtaani'

# Update the person's age
person['Age'] = 13

# Print the dictonary
print(person)

# Convert a string representing a number into an integer
toInt = '50'
toInt = int(toInt)

# Convert an integer into a float
toFloat = 12
toFloat = float(toFloat)

# Convert a float into a string
toString = 56.34
toString = str(toString)

# Print all the converted values
print(toInt, toFloat, toString)

a = 123.546
b = int(a)

print(b)