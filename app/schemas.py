from typing import List, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T')


class userSchema(BaseModel):
    user_id: Optional[int] = None
    userName: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
        by_alias = True

class Request(BaseModel):
    parameter: Optional[T] = Field(...)


class RequestUser(BaseModel):
    parameter: userSchema = Field(...)


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]
