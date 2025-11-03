# app/schemas.py
from typing import List, Optional, Annotated
from pydantic import BaseModel, Field, StringConstraints
from datetime import datetime

# handy aliases
LowerStr = Annotated[str, StringConstraints(strip_whitespace=True, to_lower=True)]
StrippedStr = Annotated[str, StringConstraints(strip_whitespace=True)]

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
    type: LowerStr
    value: StrippedStr
    source: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

class IOCOut(IOCIn):
    id: int
    reputation: int
    first_seen: datetime
    last_seen: datetime
