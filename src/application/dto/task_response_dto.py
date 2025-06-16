from pydantic import BaseModel, ConfigDict
from domain.enums.TaskStatus import TaskStatus


class TaskResponseDTO(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    owner_id: int

    model_config = ConfigDict(from_attributes=True)