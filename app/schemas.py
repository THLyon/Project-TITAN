from typing import List, Optional 
from pydantic import BaseModel, Field, constr
from datetime import datetime

class Token(BaseModel): 
    access_token: str
    token_type: str = "bearer"

class LoginForm(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class IOCIn(BaseModel):
    type: constr(strip_whitespace=True, to_lower=True)
    value: constr(strip_whitespace=True)
    source: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

class IOCOut(IOCIn):
    id: int
    reputation: int
    first_seen: datetime
    last_seen: datetime

