import requests
from models.session import SessionLocal
from models.notes import Note
from models.users import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UUID
from fastapi import HTTPException

db = SessionLocal()

def check_spelling(text):
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    return requests.get(url, params={'text': text})

def create_note(author_id: UUID, text: str):
    request_result = check_spelling(text)

    if len(request_result.json()) == 0:
        new_note = Note(text_note = text, author = author_id)
        db.add(new_note)
        db.commit()
        return {"status": 201,
        "result": "Запись успешна создана"}
    else:
        raise HTTPException(status_code=408, detail=request_result.json())

def view_notes(id_of_author: User):
    return db.query(Note).filter(Note.author == id_of_author.id).all()