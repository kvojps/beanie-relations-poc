from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str


class UserRequest(UserBase):
    ...


class UserResponse(UserBase):
    ...


class PostBase(BaseModel):
    title: str
    content: str
    user_id: str


class PostRequest(PostBase):
    ...


class PostResponse(PostBase):
    ...
