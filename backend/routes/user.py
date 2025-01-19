from fastapi import APIRouter
from schemas import UserCreate, UserUpdate


def init_app(database):
    global db
    db = database


router = APIRouter()

@router.post("/create")
async def create_user(data: UserCreate):
    return {"message": "create"}

@router.get("/get")
async def get_user(uid: str):
    return {"message": "create"}

@router.post("/update")
async def update_user(data: UserUpdate):
    return {"message": "create"}

@router.delete("/delete")
async def delete_user(uid: str):
    return {"message": "create"}