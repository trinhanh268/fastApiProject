from . import models, schemas
from sqlalchemy.orm import Session


def get_car(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()


def add_car(db: Session, car: schemas.CarModel):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

