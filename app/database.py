from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declaritive_base

DATABASE_URL = "sqlite:///./expenses.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thrad": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declaritive_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        