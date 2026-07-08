from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    """Shape of the data required to register a new user (the request body)."""
    email: EmailStr
    password: str


class UserRead(BaseModel):
    """Shape of the user data we send back (the response). No password field."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime