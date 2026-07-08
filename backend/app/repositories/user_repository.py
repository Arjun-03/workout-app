from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User


def get_user_by_email(db: Session, email: str) -> User | None:
    """Find a user by email. Returns the User or None if not found."""
    return db.execute(select(User).where(User.email == email)).scalar_one_or_none()


def create_user(db: Session, email: str, hashed_password: str) -> User:
    """Insert a new user row and return it."""
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user