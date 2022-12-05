from fastapi import FastAPI
from db.session import Base, engine, SessionLocal
from crud.crud import getUser, createUser, updateUser
from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from models.model import User

Base.metadata.create_all(bind=engine)
app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World with FastAPI"}

@app.get("/user", response_model=List[getUser])
async def getUserInfo(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return users

@app.post("/create", response_model=getUser)
async def createUser(create: createUser, db:Session=Depends(get_db)):
    user = User(username=create.username, age=create.age, gender=create.gender)
    db.add(user)
    db.commit()
    return user

@app.post("/update/{id}", response_model=getUser)
async def updateUser(id, update: updateUser, db:Session=Depends(get_db)):
    newUser = db.query(User).filter(User.id==id).first()

    newUser.username = update.username
    newUser.age = update.age
    newUser.gender = update.gender

    db.add(newUser)
    db.commit()
    return newUser

@app.delete("/delete/{id}")
async def deleteUser(id, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return "삭제 완료"
