from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    height: float
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def Bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2) , 2)
        return bmi

def update_patient_data(patient: Patient):
    print("Name=",patient.name)
    print("Age=",patient.age)
    print("Email=",patient.email)
    print("Height=",patient.height)
    print("Weight=",patient.weight)
    print("Married =",patient.married)
    print("ALlergies=",patient.allergies)
    print("Contact_details=",patient.contact_details)
    print("Body mass Index(BMI) = ",patient.Bmi)


patient_info = {'name': 'Apsara', 'age': 65, 'email': 'apsara143@icici.com','height':1.8, 'weight': 68.6, 'married': False,'allergies': ['pollen', 'dust'], "contact_details":{'phone': '9580333592' , 'emergency':'4903987924'}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)