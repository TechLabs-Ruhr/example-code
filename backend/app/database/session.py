from sqlalchemy.orm import Session  # noqa:

import app.models as models
from app.database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
