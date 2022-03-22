from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/car/", response_model=list[schemas.Car])
def read_car(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    cars = crud.get_car(db=db, skip=skip, limit=limit)
    return cars


@app.post("/create", response_model=schemas.Car)
def create_car(car: schemas.CarModel, db: Session = Depends(get_db)):
    return crud.add_car(db=db, car=car)