from typing import List
from beanie import Document, BackLink, Link
from pydantic import Field


class User(Document):
    name: str
    email: str
    posts: List[Link["Post"]]


class Post(Document):
    title: str
    content: str
    user: BackLink[User] = Field(original_field="posts")
