from uuid import UUID
from decimal import Decimal
from common.models import BaseModel
from sqlmodel import Field 

class Product(BaseModel, table=True):
    __tablename__ = "products"

    tenant_id: UUID = Field(foreign_key="tenants.id", index=True)

    sku: str = Field(index=True)
    name: str
    unit: str = "unit"                 # unit | kg
    cost: Decimal = Field(max_digits=12, decimal_places=2, default=0)
    price: Decimal = Field(max_digits=12, decimal_places=2, default=0)
    min_stock: Decimal = Field(default=0)
    is_active: bool = True