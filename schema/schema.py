from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


class UpdateUser(BaseModel):
    email: str


class UpdatePassword(BaseModel):
    password: str


class CreateUser(BaseModel):
    email: str
    password: str
    name: str
