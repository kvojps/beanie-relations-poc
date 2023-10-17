from fastapi import FastAPI, Request, status
from beanie import WriteRules

from models import User, Post
from serializers import UserRequest, UserResponse, PostRequest, PostResponse
from db_config import init_mongo_db

app = FastAPI()


@app.on_event("startup")
async def start_mongo_db():
    await init_mongo_db()


@app.post('/usuarios', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    user_data = User(name=user_request.name,
                     email=user_request.email, posts=[])
    user_created = await user_data.save(link_rule=WriteRules.DO_NOTHING)

    return UserResponse(name=user_created.name, email=user_created.email, posts=user_created.posts)


@app.post('/posts', response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post_request: PostRequest):
    user_found: User | None = await User.get(post_request.user_id)
    post_data = Post(title=post_request.title, content=post_request.content)

    if not user_found:
        raise ValueError("TESTE")

    user_found.posts = [post_data]
    post_created = await user_found.save(link_rule=WriteRules.WRITE)

    return PostResponse(title="post_created.title", content="post_created.content", user_id="post_request.user_id")
