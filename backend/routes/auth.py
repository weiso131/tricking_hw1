from fastapi import APIRouter

db = None

def init_app(database):
    global db
    db = database


router = APIRouter()
@router.post("/")
async def root():
    return {"message": "Hello, World!"}