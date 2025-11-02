import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from typing import Optional

from app.config import get_settings
from app.models import User
from app.deps import get_session

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(plain: str) -> str: 
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> str: 
    return pwd_context.verify(plain, hashed)

def create_access_token(sub: str, expires_minutes: int = settings.access_token_exp_minutes) -> str:
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload = {"sub": sub, "exp": expire}
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)) -> User: 
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Invalid or expired token", 
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        username = payload.get("sub")
        if not username: 
            raise credentials_exception
    except Exception: 
        raise credentials_exception
    user = db.exec(select(User).where(User.username == username)).one_or_none()
    if not user: 
        raise credentials_exception
    return user
