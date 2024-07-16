from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    username: str
