from tasks.task_model import Task
from sqlalchemy.orm import Session


class TaskRepository():
    def __init__(self, db : Session):
        self.db = db
    
    def create_task(self, task_data: dict) -> Task:
        new_task = Task(**task_data)
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task
    
    
    def get_task_by_id(self, task_id : str) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()
    
    
    def list_task(self) -> list[Task]:
        return self.db.query(Task).all()
    
  
    def update_task(self, task_id : str, update_data :dict) -> Task|None:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        
        if Task:
            for key, value in update_data.items():
                setattr(Task, key, value)
            self.db.commit
            self.db.refresh(Task)
        return task
    
   
    def delete_task(self, task_id : str) ->bool:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        return False