from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from practice import crud, models, schemas
from practice.database import SessionLocal

transportation_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@transportation_router.post("/routes/", response_model = schemas.Route)
async def add_route(route:schemas.RouteCreate, db: Session = Depends(get_db)):
    return crud.create_route(db, route)

@transportation_router.get("/routes/{route_id}", response_model = schemas.Route)
async def get_route(route_id: int, db: Session = Depends(get_db)):
    return crud.get_route(db, route_id)