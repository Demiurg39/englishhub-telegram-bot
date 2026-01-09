from datetime import datetime
from typing import Optional
from sqlalchemy import BigInteger, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    level: Mapped[str] = mapped_column(String(20), nullable=False)  # A1, A2, etc.
    name: Mapped[str] = mapped_column(String(50), nullable=False)   # e.g. "A2-Group-1"
    schedule_time: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. "Mon-Wed-Fri 18:00"
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship to Users (One-to-Many)
    students: Mapped[list["User"]] = relationship(back_populates="group")

    def __repr__(self) -> str:
        return f"<Group(name={self.name}, level={self.level})>"

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    username: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    level: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    role: Mapped[str] = mapped_column(String(20), default="student") # student, admin
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    preferred_time: Mapped[Optional[str]] = mapped_column(String(20), nullable=True) # morning, day, evening

    # Foreign Key to Group
    group_id: Mapped[Optional[int]] = mapped_column(ForeignKey("groups.id"), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    group: Mapped[Optional["Group"]] = relationship(back_populates="students")

    def __repr__(self) -> str:
        return f"<User(id={self.telegram_id}, name={self.full_name})>"

class WaitingList(Base):
    __tablename__ = "waiting_list"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    level: Mapped[str] = mapped_column(String(20))
    preferred_time: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship()

    def __repr__(self) -> str:
        return f"<WaitingList(user_id={self.user_id}, level={self.level})>"
