from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.user import router as user_router
from routes import init_app
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

dc_name = settings.dc_name
uri = settings.uri
tlsCAFileName = "mongodb-bundle.pem"
client = AsyncIOMotorClient(uri, tlsCAFile=tlsCAFileName)
db = client[dc_name]

init_app(db)


app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")