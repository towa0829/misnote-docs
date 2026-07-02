from uuid import UUID

from pydantic import BaseModel


class SubjectCreate(BaseModel):
    name: str


class SubjectUpdate(BaseModel):
    name: str


class SubjectResponse(BaseModel):
    id: UUID
    name: str

    model_config = {"from_attributes": True}
