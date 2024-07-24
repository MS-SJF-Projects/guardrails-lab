from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

path = Path(__file__).parent / "pos.db"
DATABASE_URL = f"sqlite:///{path}"

# Note that `connect_args={"check_same_thread": False}` is needed for SQLite
# https://fastapi.tiangolo.com/tutorial/sql-databases/
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    return SessionLocal()


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)
