"""
Main entry point of the Automotive FAQ Assistant API.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1.vin import router as vin_router
from app.core.config import settings
from app.core.middleware import LoggingMiddleware, SecurityHeadersMiddleware
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# Allow frontend applications to connect (React etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middlewares
app.add_middleware(LoggingMiddleware)
app.add_middleware(SecurityHeadersMiddleware)

# Register global exception handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Include API routes
app.include_router(vin_router)


@app.get("/", tags=["Health"])
async def health_check():
    """
    Simple health check endpoint to verify API is running.
    """
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }
