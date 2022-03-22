from sqlalchemy import String, Column, Integer
from .database import Base


class Car(Base):
    __tablename__ = 'Car'

    name = Column(String, nullable=False)
    type = Column(String, nullable=True)
    price = Column(Integer, nullable=True)
    car_id = Column(Integer, primary_key=True)
