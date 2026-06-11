from pydantic import BaseModel ,EmailStr , AnyUrl, Field
from typing import List, Dict , Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str , Field(max_length=25 , title='Name of the patient' , description='The name of the patient' , examples=['Akash ', 'Amit'])]
    age:int
    email:EmailStr
    linkedin_url:AnyUrl
    weight:Annotated[float , Field(gt=25 , lt=86 , strict=True)]
    married:Annotated[bool , Field(None, description='Is the patient married?')]
    allergies:Optional[List[str]]= None
    contact_details:Dict[str, str]

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)

patient_info = {'name':'Apsara' , 'age':21 , 'email':'apsara143@gmal.com' , 'linkedin_url':'https://www.linkedin.com/in/apsara' , 'weight':68.6 , 'married':False , 'allergies':['pollen', 'dust'] , 'contact_details':{'email':'apsara123@gmail.com' , 'phone':'9580333592'}}


patient1 = Patient(**patient_info)
update_patient_data(patient1)