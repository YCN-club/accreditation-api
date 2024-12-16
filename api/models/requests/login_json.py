from pydantic import BaseModel


class LoginJSON(BaseModel):
    username: str
    password: str

