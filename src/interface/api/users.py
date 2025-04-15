from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.application.service.task_service import UserService
from application.dto.user_create_dto import UserCreateDTO
from infrastructure.database.config import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user_dto: UserCreateDTO, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user_dto)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user