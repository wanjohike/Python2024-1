class Patient():
    def __init__(self, name, age, patient_id, ailment, admitted=False):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.ailment = ailment
        self.admitted = admitted

        def __str__(self):
            status = "Admitted" if self.admitted else "Not Admitted"
            return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Ailment: {self.aliment}, Status: {status}"
