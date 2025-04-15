from pydantic import BaseModel
from domain.enums.UserStatus import UserStatus

class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str
    is_active: UserStatus = UserStatus.ACTIVE  # default to ACTIVE if not provided