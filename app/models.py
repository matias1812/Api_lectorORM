from sqlalchemy import  Column, Integer, String
from config import Base

class Users(Base):
    __tablename__ ="user"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String)
    password = Column(String)
class Pruebas(Base):
    __tablename__ ="pruebas"

    id = Column(Integer, primary_key=True, index=True)
    qr = Column(String)
    nota = Column(String)
    prueba = Column(String)
