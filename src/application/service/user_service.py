from sqlalchemy.orm import Session
from domain.models.user import User  # Adjust import if needed
from application.dto.user_create_dto import UserCreateDTO

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_dto: UserCreateDTO):
        user = User(**user_dto.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()