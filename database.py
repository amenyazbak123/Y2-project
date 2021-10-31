from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# TODO: Add your database functions below this line!
def add_user(fullname,gmail,password):
  user = User(
    fullname = fullname,
    gmail = gmail,
    password = password)
  session.add(user)
  session.commit()
  
def query_by_name(their_name):
   user = session.query(
       User).filter_by(
       fullname=their_name).first()
   return user
   
def query_by_password(their_pass):
   user = session.query(
       User).filter_by(
       password=their_pass).first()
   return user.password





def query_all():
  return session.query(User).all()