import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

#DATABASE_URL = "sqlite:///database/tasks.db"

# Para Dockerfile con sqlite
# DATABASE_URL = "sqlite:///./tasks.db"

# Dockercompose con PostgreSQL
#DATABASE_URL = (
#    "postgresql+psycopg://"
#    "fastapi_user:"
#    "mi_password@"
#    "db:5432/"
#    "mydb"
#)

# Para desarrollo local con sqlite
#engine = create_engine(
#    DATABASE_URL, 
#    connect_args={"check_same_thread": False}
#)

# Para Dockerfile con postgresql
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False
)

Base = declarative_base()

def get_db():
    """Devuelve una sesión de base de datos para su uso en dependencias de FastAPI."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()