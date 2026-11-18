from typing import Generic, List, Sequence, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginationParams(BaseModel):

    page: int = Field(1, ge=1, description="Pages number (1-based)")
    page_size: int = Field(20, ge=1, le=100, description="Elements per page")

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        return self.page_size


class PaginatedResponse(BaseModel, Generic[T]):

    items: List[T]
    total: int
    page: int
    page_size: int
    pages: int

    @classmethod
    def from_items(
        cls,
        items: Sequence,
        total: int,
        params: PaginationParams,
    ) -> "PaginatedResponse[T]":
        pages = (total + params.page_size - 1) // params.page_size if total else 0
        return cls(
            items=list(items),
            total=total,
            page=params.page,
            page_size=params.page_size,
            pages=pages,
        )