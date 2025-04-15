from pydantic import BaseModel, Field
from domain.enums.TaskStatus import TaskStatus

class TaskCreateDTO(BaseModel):
    title: str
    description: str
    owner_id: int
    status: TaskStatus = Field(
        default=TaskStatus.PENDING,
        description="Task status. Possible values: 'pending', 'in_progress', 'completed'."
    )