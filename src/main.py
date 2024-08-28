from fastapi import FastAPI, Depends, HTTPException, status
from auth.jwt import create_jwt_token, verify_token
from fastapi.security import OAuth2PasswordBearer
from utils import users, notes
from dto.loginDto import UserCredentials
from dto.noteDto import NoteCredentials

app = FastAPI(debug=True)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/notes")
def get_notes_of_currnet_user(token:str = Depends(oauth2_scheme)):
    decoded_data = verify_token(token)
    login = decoded_data["sub"]
    user = users.find_user(login)
    return notes.view_notes(user)

@app.post("/login")
def authorize_user(login_credentials: UserCredentials):
    if (users.check_user(login_credentials.login, login_credentials.password)):
        return {"Ваш JWT-Токен:": create_jwt_token(login_credentials.login),
                "Для выполнения последующих операций:": "Требуется во вкладке Authorization выбрать Bearer Token -> и ввести токен ^"}
    else:
        raise HTTPException(status_code=403, detail="Wrong login or password")
    
@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_note(note_credentials: NoteCredentials, token:str = Depends(oauth2_scheme)):
    decoded_data = verify_token(token)
    login = decoded_data["sub"]
    user = users.find_user(login)
    return notes.create_note(user.id, note_credentials.text_note)