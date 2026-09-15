from pydantic import BaseModel, EmailStr, AnyUrl, Field,field_validator
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    #   to check the domain of email
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')

        return value

    #   to check the name:
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
        


def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
    print('updated')




patient_info={'name':'ishaan',
              'email':'xyz@hdfc.com',
              'age':21,
              'weight':90,
              'married':False,
              'allergies':['peanuts','dust'],
              'contact_details':{'email':'xyz',
                                 'address':'abc'}}

patient_1=patient(**patient_info)

update_patient_data(patient_1)
