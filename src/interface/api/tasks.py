from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.application.service.task_service import TaskService
from application.dto.task_create_dto import TaskCreateDTO
from application.dto.task_update_dto import TaskUpdateDTO
from infrastructure.database.config import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(task_dto: TaskCreateDTO, db: Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.create_task(task_dto)

@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task_service = TaskService(db)
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}")
def update_task(task_id: int, task_dto: TaskUpdateDTO, db: Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.update_task(task_id, task_dto)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.delete_task(task_id)