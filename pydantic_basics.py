# pydantic is used for data validation in python
# Here is a sample program to resolve the problem of incorrect data type not in pydantic
def insert_student_details(name:str,age:int): # This technique is good but not scalable 
    if type(name)==str and type(age)==int :
        if age<0:
            raise ValueError("Age cannot be neagative")
        else:
         print(name)
         print(age)
         print("Successfully inserted into DB")
    else :
        raise TypeError("Invalid datatype")

insert_student_details('Prem',19)

from pydantic import BaseModel

class patient(BaseModel) :
   name : str
   age : int