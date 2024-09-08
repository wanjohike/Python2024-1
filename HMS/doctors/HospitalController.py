from patients.patient import Patient
from wards.hospital import Hospital

class HMSInterface:
    def __init__(self):
        self.hospital = Hospital()

    def main(self):
        while True:
            print("Hospital Management System")
            print("1. Admit a new patient")
            print("2. Discharge a patient")
            print("3. Find a patient")
            print("4. List a patient")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter patient's name: ")
                age = int(input("Enter patient's age: "))
                patient_id = input("Enter patient ID: ")
                ailment = input("Enter patient's ailment: ")
                patient = Patient(name, age, patient_id, ailment)
                self.hospital.admit_patient(patient)

            elif choice == "2":
                patient_id = input("Enter patient ID to discharge: ")
                self.hospital.discharge_patient(patient_id)

            elif choice == "3":
                patient_id = input("Enter patient ID to discharge: ")
                self.hospital.discharge_patient(patient_id)
                if patient:
                    print(f"Patient of Patient Id {patient.patient_id}\n"
                        f"Patient's name: {patient.name}\n"
                        f"Patient's age: {patient.age}\n"
                        f"Patient's ailment: {patient.age}\n"
                        f"Patient's Admission status: {'Yes' if patient.admitted else 'No'}")
                else:
                    print(f"Patient not found")

            elif choice == "4":
                self.hospital.list_patients()

            elif choice == "5":
                print("Exiting the system")
                break
            
            else:
                print("Invalid choice. Please try again.")