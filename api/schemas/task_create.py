from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date

class TaskCreate(BaseModel):
    titulo: str = Field(
                min_length=3, 
                max_length=100, 
                description="Título de la tarea")
    contenido: str = Field(
                min_length=1, 
                max_length=500, 
                description="Contenido de la tarea")
    deadline: date = Field(description="Fecha de vencimiento")

    @field_validator('contenido')
    def contenido_validator(cls, v):
        if not v.strip():
            raise ValueError("El contenido no puede estar vacío")
        return v

    @field_validator('titulo')
    def titulo_validator(cls, v):
        if not v.strip():
            raise ValueError("El título no puede estar vacío")
        return v

    @field_validator("titulo")
    def titulo_with_values(cls, value):
        if not any(vowel in value for vowel in ["a", "e", "i", "o", "u"]):
            raise ValueError("Tu necesitas vocales en el título!")
        return value