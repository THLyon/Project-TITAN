from typing import Optional, List
from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.sqlite import JSON as SQLITE_JSON
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password_hash: str
    is_active: bool = True

class IOC(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str = Field(index=True)
    value: str = Field(index=True)
    source: Optional[str] = None
    tags: List[str] = Field(default_factory=list, sa_column=Column(SQLITE_JSON))
    reputation: int = 0  # add to match IOCOut
    first_seen: datetime = Field(default_factory=datetime.utcnow)
    last_seen: datetime = Field(default_factory=datetime.utcnow)
