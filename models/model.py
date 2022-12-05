from sqlalchemy import Column, Integer, String
from db.session import Base

class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
