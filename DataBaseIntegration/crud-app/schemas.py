from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    name:str
    email:EmailStr


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    # email:Optional[EmailStr]
    pass

class EmployeeOut(EmployeeBase):
    id:int

    class Config:
        orm_mode = True

