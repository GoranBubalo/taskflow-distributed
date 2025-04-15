from infrastructure.celery_config import celery_app
from domain.enums.TaskStatus import TaskStatus
from sqlalchemy.orm import Session
from infrastructure.database.config import get_db
from domain.repositories.task_repository import TaskRepository

@celery_app.task
def process_task(task_id: int):
    db: Session = next(get_db())
    task_repo = TaskRepository(db)

    task = task_repo.get_task(task_id)
    if task:
        task.completed = TaskStatus.COMPLETED  # Example: Mark as completed
        task_repo.update_task(task)
    return f"Task {task_id} processed successfully!"