# app/crud/user.py
from sqlmodel import Session, select
from app.models.user import User
from typing import List, Optional

class UserCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get(self, user_id: int) -> Optional[User]:
        return self.db.get(User, user_id)

    def list_users(self) -> List[User]:
        statement = select(User)
        results = self.db.exec(statement)
        return results.all()

