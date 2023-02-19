from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

if settings.DB_TYPE == "sqlite":
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
elif settings.DB_TYPE == "postgresql":
    SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"  # noqa: E501
else:
    raise ValueError(f"{settings.DB_TYPE} not specified in database.py")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # , connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
