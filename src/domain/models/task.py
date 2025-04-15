from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from domain.enums.TaskStatus import TaskStatus

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    completed = Column(SQLAlchemyEnum(TaskStatus), default=TaskStatus.PENDING)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='tasks')