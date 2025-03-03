from tasks.task_model import Task
from tasks.task_repository import TaskRepository
from sqlalchemy.orm import Session
from typing import Optional, List
from core.enums.task_status import TaskStatus
 
 #TODO :: Refactor Service layer - > Add more logic 
class TaskService():
     
    def __init__(self, db : Session):
        self.task_repository = TaskRepository(db)
        
    def create_task(self, task_data : dict) -> Task:
        if not task_data.get("title"):
            raise ValueError("Title is required for creating a task")
        
        return self.task_repository.create_task(task_data)
    
    def get_task_by_id (self, task_id :str) ->Task|None:
        return self.task_repository.get_task_by_id(task_id)
    
    
    def list_all_tasks (self) -> List[Task]:
        return self.task_repository.list_task()
    
    def update_task(self, task_id  : str, updated_data : dict) -> Optional[Task]:
        if "status" in updated_data and updated_data["status"] not in TaskStatus:
            raise ValueError("Invalid task status")
        
        return self.task_repository.update_task(task_id, updated_data)
    
    def delete_task(self, task_id : str) -> bool:
        return self.task_repository.delete_task(task_id)