# username = input('Enter username: ')
# password = input('Enter password😂: ')



# # print('Username cannot be empty') if username == "" else username
# # print('invalid password!') if len(password) < 8 else password

# if username == "":
#     if int(len(password)) < 8:
#         print
#     print('Invalid email')


# Password criteria:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
while True:
    password = input("Enter your password: ")

    # Check if the password meets the length requirement
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue
    
    # Initialize flags
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
    
    # Validate the password based on the flags
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    elif not has_lower:
        print("Password must contain at least one lowercase letter.")
    elif not has_digit:
        print("Password must contain at least one digit.")
    else:
        print("Password is valid!")
        break  # Exit the loop if the password is valid


