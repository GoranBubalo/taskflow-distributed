from pydantic import BaseModel
from src.domain.enums.TaskStatus import TaskStatus


class TaskResponseDTO(BaseModel):
    id: int
    title: str
    description: str
    completed: TaskStatus
    owner_id: int

    class Config:
        orm_mode = True