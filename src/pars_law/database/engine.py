from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

def create_database(database_url: str):
    if database_url.startswith("sqlite:///"):
        Path("data").mkdir(exist_ok=True)
    return create_engine(database_url, future=True)

def create_session_factory(database_url: str):
    engine = create_database(database_url)
    return engine, sessionmaker(bind=engine, autoflush=False, autocommit=False)
