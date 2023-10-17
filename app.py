from fastapi import FastAPI, Request, status

from serializers import UserRequest, UserResponse
from db_config import init_mongo_db

app = FastAPI()


@app.on_event("startup")
async def start_mongo_db():
    await init_mongo_db()


@app.post('/usuario', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserRequest):
    ...
