from fastapi import FastAPI

from api.controllers import task_controller
from api.core.logging import setup_logging
from api.exceptions.handlers import register_exception_handlers
from api.middleware.logging_middleware import log_requests
from api.core.database import Base, engine

app = FastAPI(
    title="Task Management API", 
    version="1.0.0"
    )

app.include_router(
    task_controller.router
)

register_exception_handlers(app)

setup_logging()

Base.metadata.create_all(bind=engine)

app.middleware("http")(log_requests)

