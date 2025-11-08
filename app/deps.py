from contextlib import contextmanager
from typing import Iterator
from sqlmodel import SQLModel, Session, create_engine
from app.config import get_settings

settings = get_settings()
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, echo=False, connect_args=connect_args)
SQLModel.metadata.create_all(engine)

@contextmanager
def session_context() -> Iterator[Session]: 
    with Session(engine) as session: 
        yield session

def get_session() ->  Iterator[Session]:
    with session_context() as s: 
        yield s

