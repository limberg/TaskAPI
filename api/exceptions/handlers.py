from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from api.exceptions.task_exceptions import TaskAlreadyCompletedException, TaskDeadlineInPastException, TaskNotFoundException

def register_exception_handlers(app: FastAPI):
    """Registra los manejadores de excepciones personalizados en la aplicación."""

    @app.exception_handler(TaskNotFoundException)
    async def task_not_found_exception_handler(
        request: Request, exc: TaskNotFoundException):
        """Manejador de excepciones para TaskNotFoundException."""
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": exc.message
            }
        )

    @app.exception_handler(TaskAlreadyCompletedException)
    async def task_already_completed_exception_handler(
        request: Request, exc: TaskAlreadyCompletedException):
        """Manejador de excepciones para TaskAlreadyCompletedException."""
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": exc.message
            }
        )

    @app.exception_handler(TaskDeadlineInPastException)
    async def task_deadline_in_past_exception_handler(
        request: Request, exc: TaskDeadlineInPastException):
        """Manejador de excepciones para TaskDeadlineInPastException."""
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": exc.message
            }
        )
