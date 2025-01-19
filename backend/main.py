from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.user import router as user_router
from routes import init_app
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['database']

init_app(db)


app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")