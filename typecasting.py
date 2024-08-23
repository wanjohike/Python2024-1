# converting integer to float
num1 = 123
num2 = 12.4
num3 = num1 + num2

print("Value:", num3, "is of data type", type(num3))

# explict convertion type - forced convertion to any build-in functions like int(), float()
#  this is by default what we then reffer to as typecasting
# We 'cast'(change) the data type top any other type

num1 = '12'
num2 = 12

# convert num1 to int
num1 = int(num1)
# check the new data type for num1
print("Data type num1: ", type(num1))