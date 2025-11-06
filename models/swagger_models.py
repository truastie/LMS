from typing import Optional
from pydantic import BaseModel, field_validator

# class RegistrationModel(BaseModel):
#     userName: str
#     password: str
#
# class RegistrationResponseModel(BaseModel):
#     value: True

class LoginModel(BaseModel):
    userName: str
    password: str

class LoginResponseModel(BaseModel):
    root: bool

class AddingBookModel(BaseModel):
    userId: str

class AddingBookResponseModel(BaseModel):
    isbn: str