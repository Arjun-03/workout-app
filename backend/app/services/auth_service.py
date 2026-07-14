from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, create_access_token
from app.repositories import user_repository
from app.schemas.user import UserCreate
from app.models.user import User


class EmailAlreadyExistsError(Exception):
    """Raised when trying to register an email that already exists."""

class InvalidCredentialsError(Exception):
    """Raised when email/password don't match a user."""

def register_user(db: Session, data: UserCreate) -> User:
    # Business rule: no two accounts may share an email.
    existing = user_repository.get_user_by_email(db, data.email)
    if existing is not None:
        raise EmailAlreadyExistsError()

    # Never store the plain password — hash it first.
    hashed = hash_password(data.password)

    return user_repository.create_user(db, email=data.email, hashed_password=hashed)

def login_user(db: Session, email: str, password: str) -> str:
    user = user_repository.get_user_by_email(db, email)

    # Same error whether the email is unknown OR the password is wrong.
    if user is None or not verify_password(password, user.hashed_password):
        raise InvalidCredentialsError()

    return create_access_token(user.id)