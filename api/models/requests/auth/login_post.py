from pydantic import BaseModel


class LoginPost(BaseModel):
    username: str
    password: str
