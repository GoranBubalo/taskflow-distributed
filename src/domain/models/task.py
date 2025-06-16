from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from domain.models.user import User
from sqlalchemy.orm import relationship
from domain.enums.TaskStatus import TaskStatus
from domain.models.base import Base  # <-- Import the shared Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    status = Column(SQLAlchemyEnum(TaskStatus), default=TaskStatus.PENDING)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='tasks')