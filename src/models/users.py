from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import  Column, UUID, String
import uuid

class Base(DeclarativeBase): pass

class User(Base):

    __tablename__ = "user"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)