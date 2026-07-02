from collections.abc import Generator
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import SessionLocal

# Phase 3 で JWT 由来の user_id に差し替える差し込み口
SEED_USER_ID = UUID("00000000-0000-0000-0000-000000000001")


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user_id() -> UUID:
    return SEED_USER_ID
