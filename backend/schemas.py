from typing import Union, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password: str
    email: str
    phone: str
    sex: bool
    age: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    uid: str

class UserUpdate(User):
    name: Optional[str]
    password: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    sex: Optional[bool]
    age: Optional[int]