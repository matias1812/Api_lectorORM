from sqlalchemy import  Column, Integer, String
from config import Base

class Users(Base):
    __tablename__ ="user"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String)
    password = Column(String)