from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Startup
    await init_db()
    yield
    # Shutdown (cleanup if needed)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="VeyraCore - AI Service Orchestration Platform",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }


# ============================================
# Route Mounting Points
# ============================================

# Auth routes (placeholder for now)
# from app.api.auth import router as auth_router
# app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

# User routes
# from app.api.users import router as users_router
# app.include_router(users_router, prefix="/api/users", tags=["users"])

# AI service routes
# from app.api.ai_services import router as ai_services_router
# app.include_router(ai_services_router, prefix="/api/ai", tags=["ai-services"])

# Task routes
# from app.api.tasks import router as tasks_router
# app.include_router(tasks_router, prefix="/api/tasks", tags=["tasks"])
