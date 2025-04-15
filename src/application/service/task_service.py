from domain.repositories.task_repository import TaskRepository
from application.dto.task_create_dto import TaskCreateDTO
from application.dto.task_update_dto import TaskUpdateDTO
from application.dto.task_response_dto import TaskResponseDTO
from domain.enums.TaskStatus import TaskStatus

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_task(self, task_id: int) -> TaskResponseDTO:
        task = self.task_repository.get_task(task_id)
        if not task:
            raise Exception(f"Task with ID {task_id} not found")
        return TaskResponseDTO.model_validate(task)

    def get_tasks_by_user(self, user_id: int) -> list[TaskResponseDTO]:
        tasks = self.task_repository.get_tasks_by_user(user_id)
        return [TaskResponseDTO.model_validate(task) for task in tasks]

    def create_task(self, task_dto: TaskCreateDTO, owner_id: int) -> TaskResponseDTO:
        task = Task(
            title=task_dto.title,
            description=task_dto.description,
            owner_id=owner_id,
        )
        created_task = self.task_repository.create_task(task)
        return TaskResponseDTO.model_validate(created_task)

    def update_task(self, task_id: int, task_dto: TaskUpdateDTO) -> TaskResponseDTO:
        task = self.task_repository.get_task(task_id)
        if not task:
            raise Exception(f"Task with ID {task_id} not found")
        if task_dto.title:
            task.title = task_dto.title
        if task_dto.description:
            task.description = task_dto.description
        if task_dto.completed:
            task.completed = task_dto.completed
        updated_task = self.task_repository.update_task(task)
        return TaskResponseDTO.model_validate(updated_task)

    def delete_task(self, task_id: int) -> TaskResponseDTO:
        task = self.task_repository.delete_task(task_id)
        if not task:
            raise Exception(f"Task with ID {task_id} not found")
        return TaskResponseDTO.model_validate(task)