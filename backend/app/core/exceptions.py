"""LIFEOS — Centralized exception definitions."""

from __future__ import annotations

from typing import Any, Optional


class LifeOSError(Exception):
    """Base exception for all LIFEOS errors."""

    def __init__(
        self,
        message: str = "An unexpected error occurred",
        status_code: int = 500,
        detail: Optional[Any] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.detail = detail
        super().__init__(message)


class NotFoundError(LifeOSError):
    """Resource not found."""

    def __init__(self, resource: str = "Resource", identifier: Any = None):
        msg = f"{resource} not found"
        if identifier:
            msg = f"{resource} with id '{identifier}' not found"
        super().__init__(message=msg, status_code=404)


class AlreadyExistsError(LifeOSError):
    """Resource already exists."""

    def __init__(self, resource: str = "Resource", field: str = ""):
        msg = f"{resource} already exists"
        if field:
            msg = f"{resource} with this {field} already exists"
        super().__init__(message=msg, status_code=409)


class AuthenticationError(LifeOSError):
    """Authentication failure."""

    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message=message, status_code=401)


class AuthorizationError(LifeOSError):
    """Authorization failure."""

    def __init__(self, message: str = "Permission denied"):
        super().__init__(message=message, status_code=403)


class ValidationError(LifeOSError):
    """Validation failure."""

    def __init__(self, message: str = "Validation failed", detail: Any = None):
        super().__init__(message=message, status_code=422, detail=detail)


class IntegrationError(LifeOSError):
    """External integration failure."""

    def __init__(self, provider: str, message: str = "Integration error"):
        super().__init__(
            message=f"{provider}: {message}",
            status_code=502,
        )


class ConfigurationError(LifeOSError):
    """Missing or invalid configuration."""

    def __init__(self, message: str = "Configuration error"):
        super().__init__(message=message, status_code=500)

