"""LIFEOS — Insurance policy model."""

from __future__ import annotations

from datetime import date
from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import Date, Enum, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDMixin


class PolicyType(str, PyEnum):
    HEALTH = "health"
    LIFE = "life"
    VEHICLE = "vehicle"
    TRAVEL = "travel"
    HOME = "home"
    OTHER = "other"


class PolicyStatus(str, PyEnum):
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"
    PENDING = "pending"


class PaymentFrequency(str, PyEnum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"
    ONE_TIME = "one_time"


class InsurancePolicy(Base, UUIDMixin, TimestampMixin):
    """Insurance policy."""

    __tablename__ = "insurance_policies"

    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    policy_type: Mapped[str] = mapped_column(Enum(PolicyType, native_enum=False), nullable=False)
    provider: Mapped[str] = mapped_column(String(255), nullable=False)
    policy_name: Mapped[str] = mapped_column(String(255), nullable=False)
    policy_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    coverage_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    premium_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    payment_frequency: Mapped[str] = mapped_column(
        Enum(PaymentFrequency, native_enum=False), default=PaymentFrequency.ANNUAL, nullable=False
    )
    start_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    expiry_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    renewal_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(
        Enum(PolicyStatus, native_enum=False), default=PolicyStatus.ACTIVE, nullable=False
    )
    nominee: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    contact_info: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    document_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

