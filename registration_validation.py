# username = input('Enter Username: ')
# email = input('Enter Email: ')
# password = input('Enter Password: ')

# if username == "":
#     print('The field cannot be empty.')
# elif email != email.find('@'):
#     print('invalid email.')
# elif password < password(len(8)):
#     print('Password must be more than 8 charters')
# else:
#     print('Login Successful!')

username = input('Enter username: ')
email = input('Enter email: ')
password = input('Enter password😂: ')

# validate the username is not empty
if username == "":
        print("Username cannot be empty")
elif "@" not in email:
        print('Invalid email!')
elif len(password) < 8:
        print('Password must contain more than 8 characters')
else:
        print('Registration Successful🤦‍♀️')
