from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories import user_repository
from app.schemas.user import UserCreate
from app.models.user import User


class EmailAlreadyExistsError(Exception):
    """Raised when trying to register an email that already exists."""


def register_user(db: Session, data: UserCreate) -> User:
    # Business rule: no two accounts may share an email.
    existing = user_repository.get_user_by_email(db, data.email)
    if existing is not None:
        raise EmailAlreadyExistsError()

    # Never store the plain password — hash it first.
    hashed = hash_password(data.password)

    return user_repository.create_user(db, email=data.email, hashed_password=hashed)