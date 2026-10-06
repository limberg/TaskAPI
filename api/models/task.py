from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from api.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    contenido = Column(String, nullable=False)
    deadline = Column(Date, nullable=False)
    completada = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, nullable=False)

    