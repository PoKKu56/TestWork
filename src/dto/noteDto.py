from pydantic import BaseModel

class NoteCredentials(BaseModel):
    text_note: str