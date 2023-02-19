from enum import Enum

from pydantic import BaseSettings


class DB_TYPE(str, Enum):
    POSTGRES = "postgres"
    SQLITE = "sqlite"


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class Backend(Settings):
    DB_TYPE: str = "sqlite"  # ToDo enforce enum above - default is sqlite to reduce additional dependencies
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_DATABASE: str = "postgres"

    HOST: str = "127.0.0.1"
    PORT: int = 8000
    RELOAD: bool = True
    DEBUG: str = "info"
    WORKERS: int = 1


settings = Backend()
