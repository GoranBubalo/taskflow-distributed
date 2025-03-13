from sqlalchemy.orm import Session
from src.domain.models.task import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_task(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_tasks_by_user(self, user_id: int):
        return self.db.query(Task).filter(Task.owner_id == user_id).all()

    def create_task(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task: Task):
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int):
        task = self.get_task(task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
        return task
