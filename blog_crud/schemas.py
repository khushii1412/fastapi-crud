from pydantic import BaseModel, EmailStr
from typing import List, Optional


# -------------------- User Schemas --------------------

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class ShowUser(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


# -------------------- Blog Schemas --------------------

class BlogBase(BaseModel):
    title: str
    content: str


class BlogCreate(BlogBase):
    pass


class ShowBlog(BlogBase):
    id: int
    author_id: int
    author: ShowUser  # nested response

    class Config:
        orm_mode = True


# -------------------- Authentication Schemas --------------------

class Login(BaseModel):
    username: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

from pydantic import BaseModel
from typing import Generic, TypeVar, List
from pydantic.generics import GenericModel

T = TypeVar("T")

class PaginatedResponse(GenericModel, Generic[T]):
    total: int
    skip: int
    limit: int
    data: List[T]


