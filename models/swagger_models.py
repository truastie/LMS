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

class AddBooksRequestModel(BaseModel):
    isbn: str

class AddingBookModel(BaseModel):
    userId: str
    collectionOfIsbns: list[AddBooksRequestModel]

class AddBooks(BaseModel):
    isbn:str

class AddingBookResponseModel(BaseModel):
    books: list[AddBooks]