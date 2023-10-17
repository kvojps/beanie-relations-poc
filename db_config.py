import motor.motor_asyncio
from beanie import init_beanie


async def init_mongo_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://mongo:mongo@localhost:27017/")
    await init_beanie(database=client['logging'], document_models=['models.User', 'models.Post'])
