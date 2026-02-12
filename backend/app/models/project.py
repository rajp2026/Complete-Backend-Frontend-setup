from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from app.models.user import User

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    owner_id: int = Field(foreign_key="user.id")

    # Back reference (not required but useful)
    owner: Optional[User] = Relationship(back_populates="projects")
