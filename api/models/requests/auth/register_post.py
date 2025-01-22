from pydantic import BaseModel


class RegisterPost(BaseModel):
    email: str
