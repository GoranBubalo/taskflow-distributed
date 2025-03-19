from pydantic import BaseModel
from src.domain.enums.UserStatus import UserStatus


class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: str
    is_active: UserStatus

    class Config:
        orm_mode = True