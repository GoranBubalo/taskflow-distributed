from sqlalchemy.orm import Session
from domain.models.user import User
from application.dto.user_create_dto import UserCreateDTO
from passlib.hash import bcrypt

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_dto: UserCreateDTO):
        hashed_pw = bcrypt.hash(user_dto.password)
        user = User(
            username=user_dto.username,
            email=user_dto.email,
            hashed_password=hashed_pw,
            is_active=user_dto.is_active  # Use the status from DTO
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()