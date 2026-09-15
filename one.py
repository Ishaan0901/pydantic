from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name:Annotated[str,
                   Field(
                       max_length=50,
                       title='name of the patient',
                       description='enter the name in less than 50 words',
                       examples=['ishaan']
                   )]
    age:int
    e_mail:EmailStr
    weight:Annotated[float,Field(
        gt=0,
        strict=True
    )]
    url:AnyUrl
    married: Optional[bool]=None

    job:Annotated[str,Field(
        default=None,
        description='enter the job title of the patient'
    )]

    allergies: List[str]=Field(max_length=5)    #here instead of normally writing list , we imported List from typing and then wrote List[str]...because if we just wrote list, then only list validation would be defined . for 2nd validation that list contains only str , we have to use List from typing module.

    contact_details: Dict[str,str]  #same reason as List

    fractures_if_any: Optional[list[str]]=None

    disease:str = 'fever'       #This is the default value of disease


def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.e_mail)
    print(patient.fractures_if_any)
    print(patient.married)
    print(patient.disease)
    print('updated')




patient_info={'name':'ishaan',
              'e_mail':'xyz@gmail.com',
              'age':21,
              'weight':90,
              'url':'http://google.com',
              'married':False,
              'allergies':['peanuts','dust'],
              'contact_details':{'email':'xyz',
                                 'address':'abc'}}

patient_1=patient(**patient_info)

update_patient_data(patient_1)