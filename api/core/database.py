from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///database/tasks.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
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