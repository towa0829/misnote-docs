from sqlalchemy.orm import Session

from app.deps import SEED_USER_ID
from app.models.user import User


def ensure_seed_user(db: Session) -> None:
    if not db.get(User, SEED_USER_ID):
        db.add(User(id=SEED_USER_ID, email="seed@misnote.local", name="シードユーザー"))
        db.commit()
