import os
from patients.patient import Patient

class Hospital():
    def __init__(self):
        self.patients = []
        self.file_path = "patientData.txt"
        self.load_patients_from_file()

    def admit_patient(self, patient):
        patient.admitted = True
        self.patients.append(patient)
        print(f"{patient.name} has been admitted.")
        self.save_patients_to_file()
    
    def discharge_patient(self, patient_id):
        patient = self.find_patient(patient_id)
        if patient:
            patient.admitted = False
            self.patients.remove(patient)
            print(f"{patient.name} has been discharged")
            self.save_patients_to_file()
        else:
            print(f"No patient found with ID {patient_id}")

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return (f"Patient \n Name {patient.name},"
                    f"\n Age: {patient.age}, \n Patient ID: {patient.patient_id},"
                    f"\n Ailment: {patient.ailment}, \n Admitted: {'Yes' if patient.admitted else 'No'} \n")
            return None
    
    def list_patients(self):
        if not self.patients:
            print("No patient in the hospital.")
        else:
            for patient in self.patients:
                print(f"Patient of Patient ID: {patient.patient_id} \n Name {patient.name},"
                    f"\n Age: {patient.age},"
                    f"\n Ailment: {patient.ailment}, \n Admitted: {'Yes' if patient.admitted else 'No'}")
    
    def save_patients_to_file(self):
        with open(self.file_path, "w") as file:
            for patient in self.patients:
                file.write(f"Patient \n Name {patient.name},"
                    f"\n Age: {patient.age}, \n Patient ID: {patient.patient_id},"
                    f"\n Ailment: {patient.ailment}, \n Admitted: {'Yes' if patient.admitted else 'No'} \n")
                
    def load_patients_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    name, age, patient_id, ailment, admitted = line.strip().strip(",")
                    patient = Patient(name, int(age), patient_id, ailment, admitted == "True")
                    self.patients.append(patient)
        else:
            print("No previous patient data found.")