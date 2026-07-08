from pwdlib import PasswordHash

# Creates a hasher preconfigured with a strong algorithm (bcrypt).
password_hash = PasswordHash.recommended()


def hash_password(plain_password: str) -> str:
    """Turn a plain password into a safe, salted hash for storage."""
    return password_hash.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a typed password against the stored hash. True if they match."""
    return password_hash.verify(plain_password, hashed_password)