from pydantic import BaseModel
from typing import Optional


class CarModel(BaseModel):
    name: str
    type: Optional[str]
    price: Optional[int]


class Car(CarModel):
    car_id: int

    class Config:
        orm_mode = True
