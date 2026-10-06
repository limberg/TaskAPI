import logging

from fastapi import APIRouter, status, Depends

from api.dependencies.dependencies import get_task_manager

from api.schemas.task_create import TaskCreate
from api.schemas.task_update import TaskUpdate
from api.schemas.task_response import TaskResponse

from api.services.task_manager import TaskManager

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

logger = logging.getLogger(__name__)

@router.get("/caducadas", response_model=list[TaskResponse])
def obtener_tareas_caducadas(
    task_manager: TaskManager = Depends(get_task_manager)):
    """Obtiene todas las tareas caducadas (con deadline pasado) y devuelve una lista de TaskResponse."""
    
    logger.info("Obteniendo tareas caducadas")

    tasks = task_manager.get_expired_tasks()
    return [
            TaskResponse(
                    id=task.id, 
                    titulo=task.titulo, 
                    contenido=task.contenido, 
                    deadline=task.deadline,
                    completada=task.completada,
                    fecha_creacion=task.fecha_creacion
                ) for task in tasks
        ]

@router.get("/{task_id}", response_model=TaskResponse)
def obtener_tarea(
                task_id: int, 
                task_manager: TaskManager = Depends(get_task_manager)):
    """Obtiene una tarea por su ID y devuelve un objeto TaskResponse."""

    logger.info("Obteniendo tarea: %s", task_id)

    task = task_manager.get_task(task_id)

    return TaskResponse(
            id = task.id,
            titulo= task.titulo,
            contenido= task.contenido,
            deadline= task.deadline,
            completada= task.completada,
            fecha_creacion= task.fecha_creacion
        )

@router.post("/", response_model=TaskResponse, 
             status_code=status.HTTP_201_CREATED)
def crear_tarea(
        task: TaskCreate, task_manager: 
        TaskManager = Depends(get_task_manager)):
    """Crea una nueva tarea y devuelve un objeto TaskResponse."""

    logger.info("Creando tarea: %s", task.titulo)

    task_created = task_manager.add_task(task)

    return TaskResponse(
        id = task_created.id,
        titulo= task_created.titulo,
        contenido= task_created.contenido,
        deadline= task_created.deadline,
        completada= task_created.completada,
        fecha_creacion= task_created.fecha_creacion
    )

@router.put("/{task_id}/completar", response_model=TaskResponse)
def marcar_completada(
        task_id: int, 
        task_update: TaskUpdate, 
        task_manager: TaskManager = Depends(get_task_manager)):
    """Marca una tarea como completada y devuelve un objeto TaskResponse."""

    logger.info("Marcando tarea como completada: %s", task_id)
    
    task = task_manager.mark_task(task_id, task_update)

    task_response = TaskResponse(
                        id=task.id, 
                        titulo=task.titulo, 
                        contenido=task.contenido, 
                        deadline=task.deadline,
                        completada=task.completada,
                        fecha_creacion=task.fecha_creacion
                    )

    return task_response

    
@router.delete("/{task_id}/eliminar",  
               status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(
            task_id:int, 
            task_manager: 
            TaskManager = Depends(get_task_manager)):
    """Elimina una tarea y devuelve un objeto TaskResponse."""

    logger.info("Eliminando tarea: %s", task_id)

    task_manager.delete_task(task_id)

    logger.info("Tarea eliminada: %s", task_id)

@router.get("/")
def root():
    """Ruta raíz de la API de gestión de tareas."""
    return {"message": "Task Management API"}
