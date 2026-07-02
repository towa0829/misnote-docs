from datetime import date
from typing import Literal
from uuid import UUID

from pydantic import BaseModel

from app.schemas.refs import QuestionRef


class MistakeNoteUpdate(BaseModel):
    memo: str | None = None
    learning: str | None = None
    next_review_at: date | None = None


class MistakeNoteStatusUpdate(BaseModel):
    status: Literal["active", "mastered"]


class MistakeNoteResponse(BaseModel):
    id: UUID
    question: QuestionRef
    memo: str | None
    learning: str | None
    status: Literal["active", "mastered"]
    wrong_count: int
    correct_streak: int
    next_review_at: date | None
