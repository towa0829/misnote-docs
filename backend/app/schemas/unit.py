from uuid import UUID

from pydantic import BaseModel


class UnitCreate(BaseModel):
    name: str


class UnitUpdate(BaseModel):
    name: str


class UnitResponse(BaseModel):
    id: UUID
    subject_id: UUID
    name: str

    model_config = {"from_attributes": True}
