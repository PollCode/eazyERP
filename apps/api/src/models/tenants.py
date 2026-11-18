from datetime import datetime
from typing import Optional

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field

from common.models import BaseModel
from models.enums import BusinessType, TenantPlan, TenantStatus


class Tenant(BaseModel, table=True):
    __tablename__ = "tenants"

    # --- Identidad del negocio ---
    name: str = Field(max_length=120, index=True)
    legal_name: Optional[str] = Field(default=None, max_length=200)
    slug: str = Field(max_length=80, unique=True, index=True)
    tax_id: Optional[str] = Field(default=None, max_length=40, index=True)
    business_type: BusinessType = Field(default=BusinessType.other)

    # --- Contacto y localización ---
    email: str = Field(max_length=255, index=True)
    phone: Optional[str] = Field(default=None, max_length=40)
    address: Optional[str] = Field(default=None, max_length=255)
    city: Optional[str] = Field(default=None, max_length=80)
    country: str = Field(default="CO", max_length=2)  # ISO 3166-1 alpha-2
    logo_url: Optional[str] = Field(default=None, max_length=500)

    # --- Configuración operativa ---
    currency: str = Field(default="USD", max_length=3)   # ISO 4217
    timezone: str = Field(default="America/Bogota", max_length=60)
    locale: str = Field(default="es", max_length=10)

    # --- Suscripción SaaS ---
    plan: TenantPlan = Field(default=TenantPlan.free)
    status: TenantStatus = Field(default=TenantStatus.trial, index=True)
    trial_ends_at: Optional[datetime] = Field(default=None)
    subscription_ends_at: Optional[datetime] = Field(default=None)

    # --- Configuración flexible ---
    settings: dict = Field(
        default_factory=dict,
        sa_column=Column(JSONB, nullable=False, server_default="{}"),
    )