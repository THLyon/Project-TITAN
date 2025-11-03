from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session 
from app.deps import get_session 
from app.models import User
from app.auth import verify_password, hash_password, create_access_token
from app.schemas import Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_session)):
    user = db.query(User).filter(User.username == username).first()
    if not user: 
        user = User(username=username, password_hash=hash_password(password))
        db.add(user)
        db.commit()
        db.refresh(user)
    elif not verify_password(password, user.password_hash): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(sub=username)
    return Token(access_token=token)