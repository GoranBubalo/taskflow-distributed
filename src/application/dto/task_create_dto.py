from pydantic import BaseModel

class TaskCreateDTO(BaseModel):
    title: str
    description: str
    owner_id : int 