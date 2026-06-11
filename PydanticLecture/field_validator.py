from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict , Optional,Annotated

class Patient2(BaseModel):
    name: str
    email: EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value

    @field_validator('name' , mode='after')
    @classmethod
    def name_validator(cls, value):
        return value.lower()


def update_patient_data(patient:Patient2):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    

patient_info = {'name':'Apsara' , 'age':21 , 'email':'apsara143@icici.com' , 'weight':68.6 , 'married':False , 'allergies':['pollen', 'dust'] ,  'phone':'9580333592'}


patient1 = Patient2(**patient_info)
update_patient_data(patient1)