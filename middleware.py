from fastapi import Request
from logger import logger

async def log_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"{response.status_code} {request.url}")
    return response