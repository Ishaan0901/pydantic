##  @computed_field in Pydantic is used when you want a field whose value is calculated from other fields instead of being directly provided by the user.


from pydantic import BaseModel, EmailStr,computed_field
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    height:float
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]


    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi


def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
    print(patient.bmi)
    print('updated')




patient_info={'name':'ishaan',
              'email':'xyz@hdfc.com',
              'age':70,
              'weight':90,
              'height':1.23,
              'married':False,
              'allergies':['peanuts','dust'],
              'contact_details':{'email':'xyz',
                                 'address':'abc',
                                 'emergency_contact':'199'}}

patient_1=patient(**patient_info)

update_patient_data(patient_1)
