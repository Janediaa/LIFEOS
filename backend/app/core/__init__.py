"""LIFEOS — Core configuration module."""

from __future__ import annotations

import secrets
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class LLMProvider(str, Enum):
    OPENAI = "openai"
    GROQ = "groq"
    GEMINI = "gemini"


class EmbeddingProvider(str, Enum):
    LOCAL = "local"
    OPENAI = "openai"
    GEMINI = "gemini"


class StorageProvider(str, Enum):
    LOCAL = "local"
    S3 = "s3"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- Application ---
    app_env: Environment = Environment.DEVELOPMENT
    debug: bool = True
    frontend_url: str = "http://localhost:5173"
    backend_url: str = "http://localhost:8000"
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    timezone: str = "Asia/Kolkata"

    # --- Database ---
    database_url: str = "sqlite+aiosqlite:///./lifeos.db"

    # --- Authentication ---
    secret_key: str = Field(default_factory=lambda: secrets.token_urlsafe(32))
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # --- LLM ---
    llm_provider: LLMProvider = LLMProvider.OPENAI
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"
    groq_api_key: Optional[str] = None
    groq_model: str = "llama-3.1-70b-versatile"
    google_api_key: Optional[str] = None
    gemini_model: str = "gemini-1.5-flash"

    # --- Embeddings ---
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_provider: EmbeddingProvider = EmbeddingProvider.LOCAL

    # --- Google OAuth ---
    google_client_id: Optional[str] = None
    google_client_secret: Optional[str] = None
    google_redirect_uri: str = "http://localhost:8000/api/v1/auth/google/callback"
    google_scopes: str = (
        "openid,email,profile,"
        "https://www.googleapis.com/auth/calendar,"
        "https://www.googleapis.com/auth/gmail.readonly"
    )

    # --- Market Data ---
    alpha_vantage_api_key: Optional[str] = None
    fmp_api_key: Optional[str] = None

    # --- Notifications ---
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_username: Optional[str] = None
    smtp_password: Optional[str] = None
    smtp_from_email: Optional[str] = None
    resend_api_key: Optional[str] = None
    telegram_bot_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None

    # --- Storage ---
    storage_provider: StorageProvider = StorageProvider.LOCAL
    upload_dir: str = "uploads"
    s3_endpoint_url: Optional[str] = None
    s3_bucket_name: Optional[str] = None
    s3_access_key_id: Optional[str] = None
    s3_secret_access_key: Optional[str] = None
    s3_region: Optional[str] = None

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @property
    def is_sqlite(self) -> bool:
        return "sqlite" in self.database_url

    @property
    def llm_api_key(self) -> Optional[str]:
        """Return the API key for the active LLM provider."""
        mapping = {
            LLMProvider.OPENAI: self.openai_api_key,
            LLMProvider.GROQ: self.groq_api_key,
            LLMProvider.GEMINI: self.google_api_key,
        }
        return mapping.get(self.llm_provider)

    @property
    def llm_model(self) -> str:
        """Return the model name for the active LLM provider."""
        mapping = {
            LLMProvider.OPENAI: self.openai_model,
            LLMProvider.GROQ: self.groq_model,
            LLMProvider.GEMINI: self.gemini_model,
        }
        return mapping.get(self.llm_provider, self.openai_model)

    @property
    def google_oauth_configured(self) -> bool:
        return bool(self.google_client_id and self.google_client_secret)

    @property
    def llm_configured(self) -> bool:
        return bool(self.llm_api_key)

    def get_integration_status(self) -> dict:
        """Return status of all integrations."""
        return {
            "llm": {
                "provider": self.llm_provider.value,
                "configured": self.llm_configured,
                "model": self.llm_model,
            },
            "google_oauth": {
                "configured": self.google_oauth_configured,
                "calendar": self.google_oauth_configured,
                "gmail": self.google_oauth_configured,
            },
            "market_data": {
                "alpha_vantage": bool(self.alpha_vantage_api_key),
                "fmp": bool(self.fmp_api_key),
            },
            "notifications": {
                "smtp": bool(self.smtp_host and self.smtp_username),
                "resend": bool(self.resend_api_key),
                "telegram": bool(self.telegram_bot_token and self.telegram_chat_id),
            },
            "storage": {
                "provider": self.storage_provider.value,
                "configured": (
                    self.storage_provider == StorageProvider.LOCAL
                    or bool(self.s3_endpoint_url)
                ),
            },
            "embeddings": {
                "provider": self.embedding_provider.value,
                "model": self.embedding_model,
                "configured": True,  # Local embeddings always available
            },
        }


# Singleton
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings

