from pydantic import BaseModel, Field
import re

class EmployeeBase(BaseModel):
    name: str = Field(..., pattern="^[A-Za-z ]+$")
    address: str
    salary: float = Field(..., gt=0)
    age: int = Field(..., gt=0)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
