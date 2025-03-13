from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.domain.enums.UserStatus import UserStatus

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(SQLAlchemyEnum(UserStatus), default=UserStatus.ACTIVE)
    tasks = relationship('Task', back_populates='owner')
