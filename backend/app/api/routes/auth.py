"""LIFEOS — Authentication API routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import CurrentUser, CurrentUserID, DBSession
from app.schemas import (
    TokenRefresh,
    TokenResponse,
    UserLogin,
    UserRegister,
    UserResponse,
    UserUpdate,
)
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(data: UserRegister, db: DBSession):
    """Register a new user account."""
    service = AuthService(db)
    return await service.register(data)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin, db: DBSession):
    """Authenticate and receive JWT tokens."""
    service = AuthService(db)
    return await service.login(data.email, data.password)


@router.post("/refresh", response_model=TokenResponse)
async def refresh_tokens(data: TokenRefresh, db: DBSession):
    """Refresh access token using a valid refresh token."""
    service = AuthService(db)
    return await service.refresh_tokens(data.refresh_token)


@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(user_id: CurrentUserID, db: DBSession):
    """Get the current authenticated user's profile."""
    service = AuthService(db)
    return await service.get_current_user(user_id)


@router.patch("/me", response_model=UserResponse)
async def update_profile(
    data: UserUpdate,
    current_user: CurrentUser,
    db: DBSession,
):
    """Update the current user's profile."""
    from app.repositories.user import UserRepository

    repo = UserRepository(db)
    if data.full_name is not None:
        current_user.full_name = data.full_name
    if data.timezone is not None:
        current_user.timezone = data.timezone
    if data.avatar_url is not None:
        current_user.avatar_url = data.avatar_url
    updated = await repo.update(current_user)
    return UserResponse.model_validate(updated)

