from pydantic import BaseModel, Field
from datetime import datetime, date

class TaskResponse(BaseModel):
    id: int = Field(description="ID de la tarea")
    titulo: str = Field(description="Título de la tarea")
    contenido: str = Field(description="Contenido de la tarea")
    deadline: date = Field(description="Fecha de vencimiento")
    completada: bool = Field(description="Estado de completado")
    fecha_creacion: datetime = Field(description="Fecha de creación de la tarea")