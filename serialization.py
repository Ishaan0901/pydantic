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

temp=patient_1.model_dump() #converts the pydantic model object to python dictionary

# temp=patient_1.model_dump(include=['name'])     #only adds name in the dictionary and leaves the rest of the things


# temp=patient_1.model_dump(exclude=['name'])       #everything except name will be added in the python dict


#temp= patient_1.model_dump(exclude={'address':['state']})  #everything except state will be added to the dict


# temp=patient_1.model_dump_json()          #converts the pydantic model object to json

print(temp)
print(type(temp))