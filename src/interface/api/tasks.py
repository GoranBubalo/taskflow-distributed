from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.service.task_service import TaskService
from application.dto.task_create_dto import TaskCreateDTO
from application.dto.task_update_dto import TaskUpdateDTO
from infrastructure.database.config import get_db
from exceptions import TaskNotFoundError, TaskCreationError, TaskUpdateError
from domain.repositories.task_repository import TaskRepository  # <-- Add this import

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(task_dto: TaskCreateDTO, db: Session = Depends(get_db)):
    try:
        task_repository = TaskRepository(db)
        task_service = TaskService(db, task_repository)
        return task_service.create_task(task_dto)
    except TaskCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task_repository = TaskRepository(db)
        task_service = TaskService(db, task_repository)
        return task_service.get_task(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{task_id}")
def update_task(task_id: int, task_dto: TaskUpdateDTO, db: Session = Depends(get_db)):
    try:
        task_repository = TaskRepository(db)
        task_service = TaskService(db, task_repository)
        return task_service.update_task(task_id, task_dto)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except TaskUpdateError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task_repository = TaskRepository(db)
        task_service = TaskService(db, task_repository)
        return task_service.delete_task(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except TaskUpdateError as e:
        raise HTTPException(status_code=400, detail=str(e))