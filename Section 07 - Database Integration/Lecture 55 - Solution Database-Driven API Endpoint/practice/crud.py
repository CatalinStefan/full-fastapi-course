from sqlalchemy.orm import Session
from practice import models, schemas

def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_route(db: Session, route: schemas.RouteCreate):
    db_route = models.Route(name=route.name, transport_type=route.transport_type, schedule=route.schedule)
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

def get_route(db: Session, route_id: int):
    return db.query(models.Route).filter(models.Route.id == route_id).first()