from fastapi import HTTPException, status

from api.exceptions.task_exceptions import TaskAlreadyCompletedException, TaskDeadlineInPastException, TaskNotFoundException
from api.schemas.task_update import TaskUpdate
from api.schemas.task_create import TaskCreate
from api.models.task import Task
from api.repositories.task_repository import TaskRepository

from datetime import datetime

class TaskManager:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, task_create: TaskCreate):
        """Agrega una nueva tarea al repositorio y devuelve la tarea creada."""
        if task_create.deadline < datetime.now().date():
            raise TaskDeadlineInPastException(task_create.deadline)
        
        task = Task(
             titulo=task_create.titulo, 
             contenido=task_create.contenido, 
             deadline=task_create.deadline, 
             completada=False, 
             fecha_creacion=datetime.now()
            )
        
        task = self.repository.create(task)

        return task

    def get_task(self, task_id:int):
        """Obtiene una tarea por su ID del repositorio y devuelve la tarea encontrada. 
           Si no se encuentra, lanza una excepción HTTP 404."""
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundException(task_id)
        
        return task
    
    def mark_task(self, task_id: int, task_upate: TaskUpdate):
        """Marca una tarea como completada o no completada según el valor de task_update.completada.
           Si la tarea no se encuentra, lanza una excepción HTTP 404."""
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundException(task_id)

        if task.completada:
            raise TaskAlreadyCompletedException(task_id)
        
        task.completada = task_upate.completada

        self.repository.update(task)

        return task


    def get_expired_tasks(self):
        """Obtiene todas las tareas caducadas (con deadline pasado) 
            del repositorio y devuelve una lista de tareas."""
        tasks = self.repository.get_expired_tasks()
        return tasks


    def delete_task(self, task_id:int):
        """Elimina una tarea por su ID del repositorio y devuelve la tarea eliminada. 
            Si no se encuentra, lanza una excepción HTTP 404."""
        task = self.repository.get_by_id(task_id)
         
        if task is None:
                raise TaskNotFoundException(task_id)

        task = self.repository.delete(task)

        return task