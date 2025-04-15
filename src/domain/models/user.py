from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from domain.enums.UserStatus import UserStatus
from domain.models.base import Base  # Use shared Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(SQLAlchemyEnum(UserStatus), default=UserStatus.ACTIVE)
    tasks = relationship('Task', back_populates='owner')