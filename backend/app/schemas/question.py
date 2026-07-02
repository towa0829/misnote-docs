from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.refs import SubjectRef, UnitRef


class QuestionCreate(BaseModel):
    subject_id: UUID
    unit_id: UUID | None = None
    question_text: str
    correct_answer: str
    memo: str | None = None
    learning: str | None = None
    next_review_at: date | None = None


class QuestionUpdate(BaseModel):
    subject_id: UUID
    unit_id: UUID | None = None
    question_text: str
    correct_answer: str


class QuestionResponse(BaseModel):
    id: UUID
    subject: SubjectRef
    unit: UnitRef | None
    question_text: str
    correct_answer: str
    created_at: datetime
    mistake_note_id: UUID | None

    model_config = {"from_attributes": True}
