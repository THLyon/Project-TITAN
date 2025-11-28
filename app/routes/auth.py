from fastapi import APIRouter, Depends, HTTPException, status, Form, select
from sqlmodel import Session 
from app.deps import get_session 
from app.models import User
from app.auth import verify_password, hash_password, create_access_token
from app.schemas import Token

router = APIRouter()

@router.post("/register")
def register(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_session)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully"}

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_session)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(sub=username)
    return Token(access_token=token)
