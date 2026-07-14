from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone

import jwt

from app.core.config import settings

ALGORITHM = "HS256"

# Creates a hasher preconfigured with a strong algorithm (bcrypt).
password_hash = PasswordHash.recommended()


def hash_password(plain_password: str) -> str:
    """Turn a plain password into a safe, salted hash for storage."""
    return password_hash.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a typed password against the stored hash. True if they match."""
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(user_id: int) -> str:
    """Create a signed JWT that proves this user's identity for a limited time."""
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload = {
        "sub": str(user_id),   # "subject" — who this token is about
        "exp": expire,         # "expiration" — when it stops being valid
    }
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)

def decode_access_token(token: str) -> int | None:
    """Verify a token and return its user_id, or None if invalid/expired."""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        return int(payload["sub"])
    except (jwt.InvalidTokenError, KeyError, ValueError):
        return None