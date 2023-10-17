from fastapi import FastAPI, Request, status
from beanie import WriteRules

from models import User, Post
from serializers import UserRequest, UserResponse
from db_config import init_mongo_db

app = FastAPI()


@app.on_event("startup")
async def start_mongo_db():
    await init_mongo_db()


@app.post('/usuario', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    user_data = User(name=user_request.name, email=user_request.email)
    user_created = await user_data.save(link_rule=WriteRules.DO_NOTHING)

    return UserResponse(name=user_created.name, email=user_created.email, posts=user_created.posts)
