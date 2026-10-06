import logging
import time
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next):
    """Middleware para registrar información sobre las solicitudes entrantes y el tiempo de respuesta."""

    start = time.time()

    response = await call_next(request)

    elapsed = time.time() - start

    logger.info(f"{request.method} {request.url.path} -> {elapsed:.3f}s")

    return response