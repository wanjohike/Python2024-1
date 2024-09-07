


# Simple user interface for interacting with the hospital system
def main():
    hospital = Hospital()

    while True:
        print("Hospital Management System")
        print("1. Admit a new patient")
        print("2. Discharge a patient")
        print("4. List a patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            patient_id = input("Enter patient ID: ")
            ailment = input("Enter patient's ailment: ")
            patient = Patient(name, age, patient_id, ailment)
            hospital.admit_patient(patient)

        elif choice == "2":
            patient_id = input("Enter patient ID to discharge: ")
            hospital.discharge_patient(patient_id)

        elif choice == "3":
            patient_id = input("Enter patient ID to discharge: ")
            hospital.discharge_patient(patient_id)
            if patient:
                print(patient)
            else:
                print("Patient not found: ")

        elif choice == "4":
            hospital.list_patients()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
