#  File        : apidevice.py
#  Project     : FELDM
#  Author      : MM
#  Description : API module to get the Device info from Devices table
######################################################################
#  Changelog :
#  24.04.2022   MM  : initial definition of  apidevice file
############################################################################
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer
from dotenv import load_dotenv
import os

# load the environmental variable from .env file
load_dotenv()
database_alchemy = os.environ.get('SQLALCHEMY_DATABASE_URL')

# create the instance of FastAPI
app = FastAPI()

# SqlAlchemy Setup

engine = create_engine(database_alchemy, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# metadata = db.MetaData()
# devices = db.Table('devices', metadata, autoload=True, autoload_with=engine)


def get_db():
    db1 = SessionLocal()
    try:
        yield db1
    finally:
        db1.close()


# A SQLAlchemny ORM Devices
class DBDevices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String(50))


Base.metadata.create_all(bind=engine)


# A Pydantic Devices
class Device(BaseModel):
    id: int
    device_name: str

    class Config:
        orm_mode = True


# Methods for interacting with the database
def get_device(db: Session, device_id: int):
    return db.query(DBDevices).where(DBDevices.id == device_id).first()


def get_devices(db: Session):
    return db.query(DBDevices).all()


# Routes for interacting with the API get all device information
@app.get('/devices/', response_model=List[Device])
def get_devices_view(db: Session = Depends(get_db)):
    return get_devices(db)


# Routes for interacting with the API get device information for particular device_id
@app.get('/device/{device_id}')
def get_device_view(device_id: int, db: Session = Depends(get_db)):
    return get_device(db, device_id)

# Just to say Hello
@app.get('/')
async def root():
    return {'FELDM': 'Hello FELDM!'}
