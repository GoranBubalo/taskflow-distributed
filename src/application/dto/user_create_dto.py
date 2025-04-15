from pydantic import BaseModel, Field
from domain.enums.UserStatus import UserStatus

class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str
    is_active: UserStatus = Field(
        default=UserStatus.ACTIVE,
        description="User status. Possible values: 'active', 'inactive'."
    )