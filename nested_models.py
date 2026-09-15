from pydantic import BaseModel

class address_class(BaseModel):
    city:str
    state:str
    pin:int

class patient(BaseModel):
    name:str
    gender:str
    age:int
    address:address_class


address_dict={
    'city':'dehradun',
    'state':'Uttarakhand',
    'pin':248011
}

address_1=address_class(**address_dict)

patient_dict={
    'name':'ravi',
    'gender':'Male',
    'age':21,
    'address':address_1
}

patient_1=patient(**patient_dict)


print(patient_1)
print(patient_1.age)
print(patient_1.address.city)