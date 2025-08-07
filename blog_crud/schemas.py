from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

# =================== User Schemas ===================

class UserBase(BaseModel):
    name: str = Field(..., description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password with at least 6 characters")

class ShowUser(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

# =================== Blog Schemas ===================
# (Leave your blog schema as-is below if any)


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


