from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    # address: str this is not a good way
    address: Address

address_info = {'city':'lucknow' , 'state':'uttar pradesh', 'pincode':'12345'}
address_data = Address(**address_info)

patient_info = {'name':'Akash chaudhary' , 'gender':'Male', 'age':21,  'address':address_data}
patient_data = Patient(**patient_info)

print(patient_data)
print(patient_data.address.city)
temp1 = patient_data.model_dump(include={'name' , 'gender' , 'age'})
print(temp1)

temp2 = patient_data.model_dump(exclude={ 'name' , 'gender' , 'age'})
print(temp2)
