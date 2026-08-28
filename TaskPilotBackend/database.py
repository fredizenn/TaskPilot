from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

CONNECTION_STRING = "postgresql://postgres:taskpilot@localhost:5434/taskpilot"
Base = declarative_base()

engine = create_engine(CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()