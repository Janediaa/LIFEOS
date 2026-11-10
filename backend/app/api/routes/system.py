"""LIFEOS — Health check and system status routes."""

from __future__ import annotations

from fastapi import APIRouter

from app.core import get_settings

router = APIRouter(tags=["System"])


@router.get("/health")
async def health_check():
    """Application health check."""
    return {"status": "healthy", "service": "lifeos-backend"}


@router.get("/status")
async def system_status():
    """Application status with integration information."""
    settings = get_settings()
    return {
        "status": "running",
        "environment": settings.app_env.value,
        "integrations": settings.get_integration_status(),
    }

