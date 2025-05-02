import uuid
from uuid import UUID

from pydantic import BaseModel, Field


class IDModelMixin(BaseModel):
    id: UUID = Field(default_factory=uuid)


class Position(IDModelMixin, BaseModel):
    name: str


class Question(IDModelMixin, BaseModel):
    name: str
    chance: str
    tag: str
    position_id: UUID
