studentList = []

def addStudent():
    # Prompt user to add student details(name, age, grade)
    while True:
        print(' ')
        print('Please add student details as prompted')
        studentName = input('Enter student name: ')
        studentAge = input('Enter student age: ')
        studentGrade = input('Enter student grade: ')
        if studentName == "" or not studentAge.isdigit or not studentAge.isdigit:
            print('Student details cannot be empty')
        

        # Convert the age and the grade to integer
        student = {
            'name': studentName,
            'age' : studentAge,
            'grade' : studentGrade
        }

        studentList.append(student)

        print(f'Student {studentName} has been added successfully\n')

        continuation = input('Do you want to continue adding student(yes/no)')
        if continuation == 'yes':
            print('Ok')
            continue
        elif continuation == 'no':
            print('Sure')
            break
        

def displayStudent():
    if not studentList:
        print(" ")
        print("No records found")
        print(" ")
        return
    
    for student in studentList:
        print(' ')
        print(f"Student Name: {student['name']}, Age: {student['age']}, Grade:{student['grade']}")

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


main()




