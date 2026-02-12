# app/api/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models.user import User
from app.crud.user import UserCRUD

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_crud(db: Session = Depends(get_session)):
    return UserCRUD(db)

@router.post("/")
def create_user(user: User, crud: UserCRUD = Depends(get_user_crud)):
    return UserCRUD.create(user)

@router.get("/")
def list_users(crud: UserCRUD = Depends(get_user_crud)):
    return UserCRUD.list_users()

@router.get("/{user_id}")
def get_user(user_id: int, crud: UserCRUD = Depends(get_user_crud)):
    user = UserCRUD.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
