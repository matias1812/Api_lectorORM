from sqlalchemy.orm import Session
from models import Users
from schemas import userSchema


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


def create_user(db: Session, user: userSchema):
    _user = Users(userName=user.userName, password=user.password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


def update_user(db: Session, user_id: int, userName: str, password: str):
    _user = db.query(Users).filter(Users.id == user_id).first()
    if _user:
        _user.userName = userName
        _user.password = password
        db.commit()
        db.refresh(_user)  # Este es el posible problema
    return _user