from users.user_model import User
from sqlalchemy.orm import Session

class UserRepository():
    
    def __init__(self, db : Session):
        self.db = db
        
    def create_user(self, user_data : dict) -> User:
        new_user = User(**user_data)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh()
        return new_user
    
    def get_user_by_id (self, user_id : str) -> User|None:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email (self, user_email : str) -> User|None: 
        return self.db.query(User).filter(User.email == user_email).first()
    
    def list_all_users (self) -> list[User]:
        return self.db.query(User).all()
    
    def update_user(self, user_id : str, update_data : dict) -> User|None:
        
        user = self.db.query(User).filter(User.id == user_id).first()
        
        if user:
            for key, value in update_data.items:
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user
    
    def delete_user (self, user_id : str) -> bool:
        user =  self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
        