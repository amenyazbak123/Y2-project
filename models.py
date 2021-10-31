from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# TODO: Add your models below this line!
class User(Base):
  __tablename__ = 'user'
  id = Column(Integer,primary_key=True)
  fullname = Column(String)
  gmail = Column(String)
  password = Column(String)
