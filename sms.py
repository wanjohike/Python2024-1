# Student management system to add and view student details
# two functions needed
# select an appropriate data structure to store the student details

# create a global function student_list to student details
# create a list
student_list = []

# function addStudent to prompts the user for name, age and grade
def addStudent():
    while True:
        # prompt user to add their details
        name = input('Enter your name: ')
        age = input('Enter your Age: ')
        grade = input('Enter your grade: ')

        # validate that the age and grade are integer
        if not age.isdigit() or not grade.isdigit():
            print('The age and grade Fields must be digit value')
            print('Please enter values again...')
            continue
        #  create a dictionary to hold the student details
        student = {
            'name' : name,
            'age' : int(age), #convert the user input age and grade into an integer
            'grade': int(grade)
        }

        # store the student details into the list we create above
        student_list.append(student)

        # create a loop for entry until the users opts out
        newStudent = input('Add anther student to the system? Y for Yes/ N for No')
        if newStudent != 'y':
            # if the key pressed is not y then, exit the loop
            break


# function to display student details
def displayStudents():
    # check for availability of student details stored in our list above
    if not student_list:
        print("No student records found!!!")
        return

    print('Students details: ')
    for student in student_list:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()

    #  main program Loop present a menu to user, allowing them to choose different
    # based on their input (1 for add new, 2 for view details, 3 for exit)


def main():
    while True:
        print('Press 1 to add student details')
        print('Press 2 to view stored Records')
        print("Press 3 to close system")

        # get the user input
        userInput = input('Please select an option: ')
        if userInput == '1':
            addStudent()
        elif userInput == '2':
            displayStudents()
        elif userInput == '3':
            break
        else:
            print('Invalid Option. Enter 1 or 2 or 3')


main()



