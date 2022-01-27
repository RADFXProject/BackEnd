from typing import List, Optional

from sqlalchemy.orm import Session

#from .schemas import GithubUser
from .models import User


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter_by(id=user_id).first()


def get_user_by_login(db: Session, usern: str) -> Optional[User]:
    return db.query(User).filter_by(email=usern).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()

#user based on DB table

def create_user(db: Session, us: User) -> User:
    user = User(
        email=us['email'],
        first_name=us['first_name'],
        last_name=us['last_name'],
        password=us['password']
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
