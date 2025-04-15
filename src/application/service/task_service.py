from sqlalchemy.orm import Session
from domain.models.task import Task
from domain.models.user import User
from domain.repositories.task_repository import TaskRepository
from domain.repositories.user_repository import UserRepository
from application.dto.task_create_dto import TaskCreateDTO
from application.dto.task_update_dto import TaskUpdateDTO
from application.dto.task_response_dto import TaskResponseDTO
from exceptions import TaskCreationError, TaskNotFoundError, TaskUpdateError

class TaskService:
    def __init__(self, task_repository: TaskRepository, user_repository: UserRepository):
        self.task_repository = task_repository
        self.user_repository = user_repository

    def get_task(self, task_id: int) -> TaskResponseDTO:
        task = self.task_repository.get_task(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        return TaskResponseDTO.model_validate(task)

    def get_tasks_by_user(self, user_id: int) -> list[TaskResponseDTO]:
        tasks = self.task_repository.get_tasks_by_user(user_id)
        return [TaskResponseDTO.model_validate(task) for task in tasks]

    def get_all_tasks(self):
        tasks = self.task_repository.get_all_tasks()
        return [TaskResponseDTO.model_validate(task) for task in tasks]

    def create_task(self, task_dto: TaskCreateDTO):
        user = self.user_repository.get_user_by_id(task_dto.owner_id)
        if not user:
            raise TaskCreationError(f"User with id {task_dto.owner_id} does not exist")
        existing_task = self.task_repository.get_task_by_owner(task_dto.owner_id)
        if existing_task:
            raise TaskCreationError(f"Task for owner_id {task_dto.owner_id} already exists")
        task = Task(
            title=task_dto.title,
            description=task_dto.description,
            owner_id=task_dto.owner_id
        )
        return self.task_repository.add_task(task)

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