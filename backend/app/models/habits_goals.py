"""LIFEOS — Habits and Goals models."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import Boolean, Date, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDMixin


class HabitFrequency(str, PyEnum):
    DAILY = "daily"
    WEEKLY = "weekly"
    CUSTOM = "custom"


class TimeOfDay(str, PyEnum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    ANY = "any"


class Habit(Base, UUIDMixin, TimestampMixin):
    """Habit definition."""

    __tablename__ = "habits"

    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    frequency: Mapped[str] = mapped_column(
        Enum(HabitFrequency, native_enum=False), default=HabitFrequency.DAILY, nullable=False
    )
    time_of_day: Mapped[str] = mapped_column(
        Enum(TimeOfDay, native_enum=False), default=TimeOfDay.ANY, nullable=False
    )
    target_days: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # e.g. "mon,wed,fri"
    streak: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    best_streak: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    color: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    icon: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    logs: Mapped[list["HabitLog"]] = relationship(back_populates="habit", cascade="all, delete-orphan")


class HabitLog(Base, UUIDMixin, TimestampMixin):
    """Habit completion log."""

    __tablename__ = "habit_logs"

    habit_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("habits.id", ondelete="CASCADE"), nullable=False, index=True
    )
    date: Mapped[date] = mapped_column(Date, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    habit: Mapped["Habit"] = relationship(back_populates="logs")


class GoalCategory(str, PyEnum):
    PERSONAL = "personal"
    CAREER = "career"
    FINANCIAL = "financial"
    LEARNING = "learning"
    HEALTH = "health"
    OTHER = "other"


class GoalStatus(str, PyEnum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    CANCELLED = "cancelled"


class Goal(Base, UUIDMixin, TimestampMixin):
    """Goal definition."""

    __tablename__ = "goals"

    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    category: Mapped[str] = mapped_column(
        Enum(GoalCategory, native_enum=False), default=GoalCategory.PERSONAL, nullable=False
    )
    status: Mapped[str] = mapped_column(
        Enum(GoalStatus, native_enum=False), default=GoalStatus.NOT_STARTED, nullable=False
    )
    target_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    progress: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    is_long_term: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    milestones: Mapped[list["GoalMilestone"]] = relationship(
        back_populates="goal", cascade="all, delete-orphan"
    )


class GoalMilestone(Base, UUIDMixin, TimestampMixin):
    """Goal milestone."""

    __tablename__ = "goal_milestones"

    goal_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("goals.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    target_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    goal: Mapped["Goal"] = relationship(back_populates="milestones")

