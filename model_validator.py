from pydantic import BaseModel, EmailStr, AnyUrl, Field,model_validator
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact number')
        return model



def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
    print('updated')




patient_info={'name':'ishaan',
              'email':'xyz@hdfc.com',
              'age':70,
              'weight':90,
              'married':False,
              'allergies':['peanuts','dust'],
              'contact_details':{'email':'xyz',
                                 'address':'abc',
                                 'emergency_contact':'199'}}

patient_1=patient(**patient_info)

update_patient_data(patient_1)
