import logging
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api_router
from config import settings

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Example REST API",
    description="This is an example application",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Add API to app
app.include_router(api_router)


# Setup event listeners
@app.on_event("startup")
async def on_startup():
    """Startup handler"""
    logger.info("Starting server")


@app.on_event("shutdown")
async def on_shutdown():
    """Shutdown handler"""
    logger.info("Shutting down server")


# Setup cors - to allow cross origin requests (e.g. from different hostnames)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level=settings.DEBUG,
        workers=settings.WORKERS,
    )
