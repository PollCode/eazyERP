from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field

from common.models import BaseModel
from models.enums import UserRole, UserStatus


class User(BaseModel, table=True):
    __tablename__ = "users"
    __table_args__ = (
        UniqueConstraint("tenant_id", "pin_hash", name="uq_users_tenant_pin"),
    )

    # --- Multi-tenancy e identidad ---
    tenant_id: UUID = Field(foreign_key="tenants.id", index=True)
    email: str = Field(max_length=255, unique=True, index=True)
    email_verified_at: Optional[datetime] = Field(default=None)

    # --- Identidad personal ---
    full_name: str = Field(max_length=150)
    phone: Optional[str] = Field(default=None, max_length=40)
    avatar_url: Optional[str] = Field(default=None, max_length=500)

    # --- Credenciales y seguridad ---
    password_hash: str = Field(max_length=255)
    email_verification_token: Optional[str] = Field(default=None, max_length=128, index=True)
    password_reset_token: Optional[str] = Field(default=None, max_length=128, index=True)
    password_reset_expires_at: Optional[datetime] = Field(default=None)
    refresh_token_hash: Optional[str] = Field(default=None, max_length=255)
    refresh_token_expires_at: Optional[datetime] = Field(default=None)
    failed_login_attempts: int = Field(default=0)
    locked_until: Optional[datetime] = Field(default=None)
    last_login_at: Optional[datetime] = Field(default=None)

    # --- Autorización y estado ---
    role: UserRole = Field(default=UserRole.cashier, index=True)
    status: UserStatus = Field(default=UserStatus.pending_verification, index=True)
    invited_at: Optional[datetime] = Field(default=None)
    invited_by: Optional[UUID] = Field(default=None, foreign_key="users.id")
    activated_at: Optional[datetime] = Field(default=None)

    # --- Operación del POS ---
    pin_hash: Optional[str] = Field(default=None, max_length=255)

    # --- Preferencias personales ---
    locale: Optional[str] = Field(default=None, max_length=10)
    timezone: Optional[str] = Field(default=None, max_length=60)
    settings: dict = Field(
        default_factory=dict,
        sa_column=Column(JSONB, nullable=False, server_default="{}"),
    )