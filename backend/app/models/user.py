from typing import List
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    is_active: bool = True

    projects: List["Project"] = Relationship(back_populates="owner")
