from fastapi import FastAPI
from interface.api import tasks, users
from infrastructure.database.config import engine
from domain.models.task import Base as TaskBase
from domain.models.user import Base as UserBase

# Create database tables
TaskBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="TaskFlow")

# Include routers
app.include_router(tasks.router)
app.include_router(users.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to TaskFlow!"}