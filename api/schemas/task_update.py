from pydantic import BaseModel, Field

class TaskUpdate(BaseModel):
    completada: bool = Field(description="Estado de completado")
