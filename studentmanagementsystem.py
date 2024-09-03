studentList = []

# Function to acquire and add a student details for a user
def addStudent():
    # Loop the process for adding student details
    while True:
        # Prompt user to add student details(name, age, grade)
        print(' ')
        print('Please add student details as prompted')
        studentName = input('Enter student name: ')
        studentAge = input('Enter student age: ')
        studentGrade = input('Enter student grade: ')
        # validate the users input of the student details
        if studentName == "" :
            if not studentAge.isdigit or not studentGrade.isdigit:
                print('Age and grade must be numbers.')
            print('Student details cannot be empty')
        
        # store the student details in a student dictionary
        student = {
            'name': studentName,
            'age' : studentAge,
            'grade' : studentGrade
        }

        # add the student dictionary to the global student list(studentList)
        studentList.append(student)

        print(f'Student {studentName} has been added successfully\n')

        # ask the user where to continue adding or stop.
        continuation = input('Do you want to continue adding student(yes/no)')
        if continuation == 'yes':
            print('Ok')
            continue
        elif continuation == 'no':
            print('Sure')
            break
        
# function to display stored students details for the global studentList
def displayStudent():
    if not studentList:
        print(" ")
        print("No records found")
        print(" ")
        return
    # Loop through while displaying each student details form the list.
    for student in studentList:
        print(' ')
        print(f"Student Name: {student['name']}, Age: {student['age']}, Grade:{student['grade']}")

# function to display a menu for the user to choose what they need
def main():
    while True:
        print('Welcome to Murima School Management System')
        print('1. To add student')
        print('2. To view student')
        print('3. Exit')
        choice = input('Please choose action you need to take: ')

        if choice == '1':
            addStudent()
        elif choice == '2':
            displayStudent()
        elif choice == '3':
            print('Adios Mchachos')
            break
        else:
            print('Please enter 1, 2, or 3 Kindly.')

# launching the program
main()




