from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import  Column, UUID, String
from .users import User
import uuid

class Base(DeclarativeBase): pass

class Note(Base):

    __tablename__ = "note"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    text_note = Column(String)
    author = Column(UUID, ForeignKey(User.id))
    author_id = relationship(User)