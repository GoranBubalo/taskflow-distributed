from user_model import User
from user_repository import UserRepository
from sqlalchemy.orm import Session
from typing import Optional, List

#TODO:: Refactor Service layer - > Add more logic 
class UserService():
    def __init__(self, db : Session):
        self.user_repository = UserRepository(db)

    def create_user(self, user_data : dict) -> User:
        if self.user_repository.get_user_by_email(user_data["emial"]):
            raise ValueError("User With email already exists")
        
        if not user_data.get("password"):
            raise ValueError("Password is required for creating a user")
        
        return self.user_repository.create_user(user_data)
    
    def get_user_by_id(self, user_id : str ) -> Optional[User]:
        return self.user_repository.get_user_by_id(user_id)
    
    def get_user_by_email(self, user_email : str) -> Optional[User]:
        return self.user_repository.get_user_by_email(user_email)

    def list_all_users (self) -> List[User]:
        return self.user_repository.list_all_users()
    
    def update_user(self, user_id : str, new_data: dict) -> Optional[User]:
        
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not Found!!")
        
        allowed_fields = {"name", "email", "is_active"}
        for key, values in new_data.items():
            if key in allowed_fields:
                setattr(user, key, values)
            
        self.user_repository.update_user(user_id, new_data)
        return user
    
    def delete_user (self, user_id : str) -> bool:
        return self.user_repository.delete_user(user_id)
    
    