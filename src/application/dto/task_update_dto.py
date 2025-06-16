from pydantic import BaseModel
from domain.enums.TaskStatus import TaskStatus

class TaskUpdateDTO(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None