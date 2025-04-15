from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.service.user_service import UserService
from domain.repositories.user_repository import UserRepository
from application.dto.user_create_dto import UserCreateDTO
from application.dto.user_update_dto import UserUpdateDTO
from infrastructure.database.config import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user_dto: UserCreateDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.create_user(user_dto)

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.get_all_users()

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user(user_id: int, user_dto: UserUpdateDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.update_user(user_id, user_dto)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.delete_user(user_id)