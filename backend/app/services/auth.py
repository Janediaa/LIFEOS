"""LIFEOS — Authentication service."""

from __future__ import annotations

import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import (
    AlreadyExistsError,
    AuthenticationError,
)
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas import (
    TokenResponse,
    UserRegister,
    UserResponse,
)


class AuthService:
    """Authentication business logic."""

    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def register(self, data: UserRegister) -> UserResponse:
        """Register a new user."""
        if await self.repo.exists_by_email(data.email):
            raise AlreadyExistsError("User", "email")
        if await self.repo.exists_by_username(data.username):
            raise AlreadyExistsError("User", "username")

        user = User(
            email=data.email.lower(),
            username=data.username,
            hashed_password=hash_password(data.password),
            full_name=data.full_name,
        )
        user = await self.repo.create(user)
        return UserResponse.model_validate(user)

    async def login(self, email: str, password: str) -> TokenResponse:
        """Authenticate user and return tokens."""
        user = await self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise AuthenticationError("Invalid email or password")
        if not user.is_active:
            raise AuthenticationError("Account is deactivated")

        access_token = create_access_token({"sub": user.id})
        refresh_token = create_refresh_token({"sub": user.id})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def refresh_tokens(self, refresh_token: str) -> TokenResponse:
        """Refresh access token using a valid refresh token."""
        try:
            payload = decode_token(refresh_token)
            if payload.get("type") != "refresh":
                raise AuthenticationError("Invalid token type")
            user_id = payload.get("sub")
            if not user_id:
                raise AuthenticationError("Invalid token payload")
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Refresh token expired")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid refresh token")

        user = await self.repo.get_by_id(user_id)
        if not user or not user.is_active:
            raise AuthenticationError("User not found or deactivated")

        new_access = create_access_token({"sub": user.id})
        new_refresh = create_refresh_token({"sub": user.id})

        return TokenResponse(
            access_token=new_access,
            refresh_token=new_refresh,
        )

    async def get_current_user(self, user_id: str) -> UserResponse:
        """Get the current authenticated user."""
        user = await self.repo.get_by_id(user_id)
        if not user or not user.is_active:
            raise AuthenticationError("User not found or deactivated")
        return UserResponse.model_validate(user)

