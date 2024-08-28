from models.users import User
from models.session import SessionLocal
from sqlalchemy import UUID

db = SessionLocal()

def check_user(login: str, password: str) -> bool:

    if db.query(User).filter(User.login == login and User.password == password).first():
        return True
    
    return False

def find_user(login: str) -> User:

    return db.query(User).filter(User.login == login).first()
