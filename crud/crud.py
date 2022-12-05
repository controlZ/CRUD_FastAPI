from pydantic import BaseModel

class getUser(BaseModel):
    id: int
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True

class createUser(BaseModel):
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True

class updateUser(BaseModel):
    username: str
    age: int
    gender: str

    class Config:
        orm_mode = True