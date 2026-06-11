from pydantic import BaseModel, EmailStr, AnyUrl, Field,  model_validator
from typing import List, Dict, Optional, Annotated


class Patient2(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have emergency contact.')
        return model


def update_patient_data(patient: Patient2):
    print(patient.name)
    print(patient.age)
    print(patient.email)


patient_info = {'name': 'Apsara', 'age': 65, 'email': 'apsara143@icici.com', 'weight': 68.6, 'married': False,
                'allergies': ['pollen', 'dust'], "contact_details":{'phone': '9580333592' , 'emergency':'4903987924'}}

patient1 = Patient2(**patient_info)
update_patient_data(patient1)