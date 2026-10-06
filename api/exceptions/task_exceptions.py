from datetime import date

class TaskNotFoundException(Exception):
    """Excepción personalizada para indicar que una tarea no se encontró en la base de datos."""
    def __init__(self, task_id: int):
        self.task_id = task_id
        self.message = f"Tarea con ID {task_id} no encontrada."
        super().__init__(self.message)

class TaskAlreadyCompletedException(Exception):
    """Excepción personalizada para indicar que una tarea ya está completada."""
    def __init__(self, task_id: int):
        self.task_id = task_id
        self.message = f"Tarea con ID {task_id} ya está completada."
        super().__init__(self.message)

class TaskDeadlineInPastException(Exception):
    """Excepción personalizada para indicar que el deadline de la tarea a crear está en el pasado."""
    def __init__(self, deadline: date):
        self.deadline = deadline
        self.message = f"Deadline {deadline} esta en el pasado."
        super().__init__(self.message)