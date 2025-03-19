from pydantic import BaseModel
from src.domain.enums.UserStatus import UserStatus

class UserUpdateDTO(BaseModel):
    username: str
    email: str | None = None
    password: str | None = None
    is_active: UserStatus | None = None