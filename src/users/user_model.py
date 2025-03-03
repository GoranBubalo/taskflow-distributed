from sqlalchemy import Column, String, Boolean, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4(), name = "user_id")
    name = Column(String(100), nullable=False, name = "name")
    email = Column(String(100), unique=True, nullable=False, name = "email")
    password = Column(String(120), nullable=False, name = "password")
    is_active = Column(Boolean, default=True, name = "is_user_active")
    created_at = Column(DateTime, default= datetime.datetime.utcnow, name = "user_created_at")
    updated_at = Column(DateTime, default= datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, name = "user_updated_at")