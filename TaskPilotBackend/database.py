from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

CONNECTION_STRING = "postgresql://postgres:taskpilot@127.0.0.1:5433/taskpilot"
Base = declarative_base()

engine = create_engine(CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)