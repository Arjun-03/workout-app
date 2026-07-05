from app.core.database import Base, engine
from app.models.user import User  # noqa: F401  (imported so the table registers)

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")