from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    name: str
    email: str
    posts: list


class PostBase(BaseModel):
    title: str
    content: str
    user_id: str


class PostRequest(PostBase):
    ...


class PostResponse(PostBase):
    ...
