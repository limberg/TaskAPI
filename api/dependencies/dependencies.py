from fastapi import Depends
from sqlalchemy.orm import Session
from api.core.database import get_db    

from api.repositories.task_repository import TaskRepository 
from api.services.task_manager import TaskManager

def get_task_repository(
        db: Session = Depends(get_db)
        ) -> TaskRepository:
    """Devuelve una instancia de TaskRepository utilizando la sesión de base de datos proporcionada."""
    return TaskRepository(db)

def get_task_manager(
        repository: TaskRepository = Depends(get_task_repository)
        ) -> TaskManager:
    """Devuelve una instancia de TaskManager utilizando el repositorio proporcionado."""
    return TaskManager(repository)