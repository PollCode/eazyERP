from typing import Optional, Type
from pydantic import BaseModel, ConfigDict
from sqlmodel import SQLModel
from sqlalchemy import Select

class BaseFilter(BaseModel):

    model_config = ConfigDict(extra="forbid")

    def apply(self, statement: Select, model: Type[SQLModel]) -> Select:
        return statement

    def order_by(self, model: Type[SQLModel]):
        return model.created_at.desc()

    def _ilike(self, column, value: Optional[str]):
        return column.ilike(f"%{value}%") if value else None


