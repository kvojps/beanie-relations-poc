from typing import List
from beanie import Document, BackLink, Link
from pydantic import Field


class Post(Document):
    title: str
    content: str
    user: Link["User"]


class User(Document):
    name: str
    email: str
    posts: List[BackLink[Post]] = Field(original_field="user")
