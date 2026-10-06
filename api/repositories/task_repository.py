import datetime

from sqlalchemy.orm import Session

from api.models.task import Task

class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, task_id: int) -> Task | None:
        """Obtiene una tarea por su ID de la base de datos. 
           Devuelve la tarea si se encuentra, o None si no se encuentra."""
        return self.db.query(Task).filter(
                    Task.id == task_id
                    ).first()

    def create(self, task: Task) -> Task | None:
        """Crea una nueva tarea en la base de datos y devuelve la tarea creada."""
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, task:Task):
        """Actualiza una tarea existente en la base de datos y devuelve la tarea actualizada."""
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_expired_tasks(self):
        """Obtiene todas las tareas caducadas (con deadline pasado) de la base de datos 
            y devuelve una lista de tareas."""
        return self.db.query(Task).filter(
             Task.deadline < datetime.datetime.now()
            ).all()

    def delete(self, task: Task):
        """Elimina una tarea de la base de datos y devuelve la tarea eliminada."""
        self.db.delete(task)
        self.db.commit()
        return task