from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# The engine manages the actual connections to Postgres.
engine = create_engine(settings.database_url, echo=True)

# A factory that produces new database sessions when called.
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

def get_db():
    """Provide a database session for one request, then close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Every model we write will inherit from this Base.
class Base(DeclarativeBase):
    pass