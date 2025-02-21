from sqlalchemy.orm import Session
from . import repository, schemas

def register_user(db: Session, user: schemas.UserCreate):
    return repository.create_user(db, user)
