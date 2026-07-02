from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.deps import get_db, get_current_user_id
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectResponse, SubjectUpdate

router = APIRouter()


@router.get("", response_model=list[SubjectResponse])
def list_subjects(
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db),
) -> list[Subject]:
    return db.query(Subject).filter(Subject.user_id == user_id).all()


@router.post("", response_model=SubjectResponse, status_code=status.HTTP_201_CREATED)
def create_subject(
    body: SubjectCreate,
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db),
) -> Subject:
    subject = Subject(user_id=user_id, name=body.name)
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject


@router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject(
    subject_id: UUID,
    body: SubjectUpdate,
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db),
) -> Subject:
    subject = db.query(Subject).filter(Subject.id == subject_id, Subject.user_id == user_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    subject.name = body.name
    db.commit()
    db.refresh(subject)
    return subject


@router.delete("/{subject_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subject(
    subject_id: UUID,
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db),
) -> None:
    subject = db.query(Subject).filter(Subject.id == subject_id, Subject.user_id == user_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    if subject.units or subject.questions:
        raise HTTPException(status_code=409, detail="Subject has related units or questions")
    db.delete(subject)
    db.commit()
