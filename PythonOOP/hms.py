class Patient():
    def __init__(self, name, age, patient_id, aliment, admitted=False):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.aliment = aliment
        self.admitted = admitted

        def __str__(self):
            status = "Admitted" if self.admitted else "Not Admitted"
            return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Ailment: {self.aliment}, Status: {status}"



class Hospital():
    def __init__(self):
        self.patients = []

    def admit_patient(self, patient):
        patient.admitted = True
        self.patients.append(patient)
        print(f"{patient.name} has been admitted.")
    
    def discharge_patient(self, patient_id):
        patient = self.find_patient(patient_id)
        if patient:
            patient.admitted = False
            self.patients.remove(patient)
            print(f"{patient.name} has been discharged")
        else:
            print(f"No patient found with ID {patient_id}")

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
            return None
    
    def list_patients(self):
        if not self.patients:
            print("No patient in the hospital.")
        else:
            for patient in self.patients:
                print(patient)


# Simple user interface for interacting with the hospital system
def main():
    hospital = Hospital()

    while True:
        print("\Hospital Managment System")
        print("1. Admit a new patient")
        print("2. Discharge a patient")
        print("4. Find a patient")
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
            hospital.discharge_patient
