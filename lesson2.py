#ask the user to enter there details
# check the datatype of the variable\
# identiy what a variable is - it is a container
# python is dynamically typed - we do not need to specify the datatype
# typecating - converting from one data type to anther

# Example getting input from user
# get the users fulname and get then comput there ages for next your


# # output their details and age next year
# print("Your name is: ", fullname, "and your current age is: ", age)
# print("Next year you shall be", age + 1)

# num1 = 5/6
# print(num1, 'is of type', type(num1))
# num2 = 2.0
# print(num2, 'is of type', type(num2))
# num3 = 1 + 2j
# print(num3, 'is of type', type(num3))

# name = 'Python '
# print(name)

# message = 'Python for beginners'
# print(message)

# create a list of 4 programming languages

print("Below are the four programming languages in my view.")
language = ["Swift", "Java", "Python", "C#"]

# access element at index 0
# print (variable name[index value])
print(language[0])
print(language[3])

# mutable vs immutable objects
# mutable objects means they caN CHANGE
# iMMUTABLE MEANS THEY CANNOT CHANGE - EXAMPLE STRING
# modifying our list
# append an element to the end of the list
# syntax list_name.append(element)
language.append("JavaScript")
print(language[4])

# insert an element into a list
# syntax list_name.insert(index, element)
print(language[2])
language.insert(2, "php")
print(language[2])

# we can also remove an element from our list
# syntax lis_name.remove(element)
# language.remove("C#")
print(language[3])

# extent the list to have Go, SQL
# syntax new_Language.extend("element1", "element2")
# Language
# create a new list of two extra languages
new_language = ["Go", "SQL"]
print(new_language[1])
# extend the list to the original
language.extend(new_language)
print(len(language))
print(language[5])