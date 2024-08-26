# # for number in [0,1,2,3,4,5,6]:
# #     print(number)

# # Using a range
# for number in range(5):
#     print(number)

# # Using a start and stop value for our loop
# # print out values between 101 and 115
# num = list(range(200, 500, 20))
# print(num)

# # # Iterate over the following string "Hello"
# # for name in "Hello":
# #     print(name)

# list = [10,20,30,40,50]
# for x in list:
#     print(x)
#     if x == 40:
#         break

# groceries = ["cabbage", "tomatoes", "potatoes", "onions", "okra", "mango", "orange"]
# for endbreak in groceries:
#     print(endbreak)
#     if endbreak == "okra":
#         break


# list = [10, 30, 200, 50, 40, 300, 60]
# for x in list:
#     if x > 100:
#         continue
#     print(x)

# We have 2 list, people and their age, we want to print each person with their age
people = ['Hayan', 'Bronson', 'Erick']
ages = [21, 24, 25]
hometowns = ['Tudor', 'Nyali', 'Mathira']
# use the for loop to find the length of our list using the length function
# print('Person', 'Age', 'Hometown')
# for position, person in enumerate(people):
#     age = ages[position]
#     town = hometowns[position]
#     print(person,age, town)

print('Person', 'Age', 'Hometown')
for person, age, hometowns in zip(people,ages, hometowns):
    print(person,age, hometowns)