"""LIFEOS — Bills and subscriptions model."""

from __future__ import annotations

from datetime import date
from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import Boolean, Date, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDMixin


class BillFrequency(str, PyEnum):
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"
    ONE_TIME = "one_time"


class BillStatus(str, PyEnum):
    ACTIVE = "active"
    PAUSED = "paused"
    CANCELLED = "cancelled"


class Bill(Base, UUIDMixin, TimestampMixin):
    """Recurring bill or subscription."""

    __tablename__ = "bills"

    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default="INR", nullable=False)
    frequency: Mapped[str] = mapped_column(
        Enum(BillFrequency, native_enum=False), default=BillFrequency.MONTHLY, nullable=False
    )
    due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    next_due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(
        Enum(BillStatus, native_enum=False), default=BillStatus.ACTIVE, nullable=False
    )
    category: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    provider: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    auto_pay: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    reminder_days: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class BillPayment(Base, UUIDMixin, TimestampMixin):
    """Record of a bill payment."""

    __tablename__ = "bill_payments"

    bill_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("bills.id", ondelete="CASCADE"), nullable=False, index=True
    )
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    paid_date: Mapped[date] = mapped_column(Date, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

