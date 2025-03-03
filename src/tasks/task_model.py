from sqlalchemy import Column, String, DateTime, UUID, TEXT, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid, datetime
from core.enums.task_status import TaskStatus
from core.enums.task_priority import TaskPriority

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4(), name = "task_id")
    title = Column(String(100), nullable=False, name = "title")
    description = Column(TEXT, nullable = True, name = "description")
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING, name = "status")
    priority = Column(Enum(TaskPriority))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), name = "user_id")
    created_at = Column(DateTime, default=datetime.datetime.utcnow, name = "task_created_at")
    updated_at = Column(DateTime,default=datetime.datetime.utcnow, onupdate= datetime.datetime.utcnow, name = "task_updated_at")