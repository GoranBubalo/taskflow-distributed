from sqlalchemy.orm import Session
from domain.models.user import User
from application.dto.user_create_dto import UserCreateDTO
from application.dto.user_update_dto import UserUpdateDTO
from passlib.hash import bcrypt
from domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_dto: UserCreateDTO):
        hashed_pw = bcrypt.hash(user_dto.password)
        user = User(
            username=user_dto.username,
            email=user_dto.email,
            hashed_password=hashed_pw,
            is_active=user_dto.is_active
        )
        return self.user_repository.add_user(user)

    def get_user(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id: int, user_dto: UserUpdateDTO):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found")
        if user_dto.username:
            user.username = user_dto.username
        if user_dto.email:
            user.email = user_dto.email
        if user_dto.is_active is not None:
            user.is_active = user_dto.is_active
        if user_dto.password:
            # hash the password before saving (replacewith your hash function if needed)
            user.hashed_password = bcrypt.hash(user_dto.password)
        return self.user_repository.update_user(user)

    def delete_user(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found")
        self.user_repository.delete_user(user_id)
        return {"detail": f"User {user_id} deleted successfully"}