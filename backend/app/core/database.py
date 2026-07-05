from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

# The engine manages the actual connections to Postgres.
engine = create_engine(settings.database_url, echo=True)

# Every model we write will inherit from this Base.
class Base(DeclarativeBase):
    pass