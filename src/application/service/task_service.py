from sqlalchemy.orm import Session
from domain.models.task import Task
from domain.repositories.task_repository import TaskRepository
from application.dto.task_create_dto import TaskCreateDTO
from application.dto.task_update_dto import TaskUpdateDTO
from application.dto.task_response_dto import TaskResponseDTO
from exceptions import TaskCreationError, TaskNotFoundError, TaskUpdateError

class TaskService:
    def __init__(self, db: Session, task_repository: TaskRepository):
        self.db = db
        self.task_repository = task_repository

    def get_task(self, task_id: int) -> TaskResponseDTO:
        task = self.task_repository.get_task(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        return TaskResponseDTO.model_validate(task)

    def get_tasks_by_user(self, user_id: int) -> list[TaskResponseDTO]:
        tasks = self.task_repository.get_tasks_by_user(user_id)
        return [TaskResponseDTO.model_validate(task) for task in tasks]

    def create_task(self, task_dto: TaskCreateDTO):
        # Check if a task with the same owner already exists
        existing_task = self.db.query(Task).filter(Task.owner_id == task_dto.owner_id).first()
        if existing_task:
            raise TaskCreationError(f"Task for owner_id {task_dto.owner_id} already exists")
        task = Task(
            title=task_dto.title,
            description=task_dto.description,
            owner_id=task_dto.owner_id
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, task_dto: TaskUpdateDTO) -> TaskResponseDTO:
        task = self.task_repository.get_task(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        try:
            if task_dto.title:
                task.title = task_dto.title
            if task_dto.description:
                task.description = task_dto.description
            if task_dto.completed:
                task.completed = task_dto.completed
            updated_task = self.task_repository.update_task(task)
            return TaskResponseDTO.model_validate(updated_task)
        except Exception as e:
            raise TaskUpdateError(f"Failed to update task with ID {task_id}: {str(e)}")

    def delete_task(self, task_id: int) -> TaskResponseDTO:
        task = self.task_repository.get_task(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        try:
            self.task_repository.delete_task(task_id)
            return TaskResponseDTO.model_validate(task)
        except Exception as e:
            raise TaskUpdateError(f"Failed to delete task with ID {task_id}: {str(e)}")