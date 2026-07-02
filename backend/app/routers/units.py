from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.deps import get_db, get_current_user_id
from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitResponse, UnitUpdate

# /v1/subjects/{subject_id}/units 配下
subjects_router = APIRouter()

# /v1/units/{id} 配下
units_router = APIRouter()


@subjects_router.get("/{subject_id}/units", response_model=list[UnitResponse])
def list_units(subject_id: UUID, db: Session = Depends(get_db)) -> list[Unit]:
    return db.query(Unit).filter(Unit.subject_id == subject_id).all()


@subjects_router.post("/{subject_id}/units", response_model=UnitResponse, status_code=status.HTTP_201_CREATED)
def create_unit(subject_id: UUID, body: UnitCreate, db: Session = Depends(get_db)) -> Unit:
    unit = Unit(subject_id=subject_id, name=body.name)
    db.add(unit)
    db.commit()
    db.refresh(unit)
    return unit


@units_router.put("/{unit_id}", response_model=UnitResponse)
def update_unit(unit_id: UUID, body: UnitUpdate, db: Session = Depends(get_db)) -> Unit:
    unit = db.get(Unit, unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    unit.name = body.name
    db.commit()
    db.refresh(unit)
    return unit


@units_router.delete("/{unit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_unit(unit_id: UUID, db: Session = Depends(get_db)) -> None:
    unit = db.get(Unit, unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    if unit.questions:
        raise HTTPException(status_code=409, detail="Unit has related questions")
    db.delete(unit)
    db.commit()
