from fastapi import APIRouter

collection = None

def init_app(db):
    global collection
    collection = db['user']


router = APIRouter()
@router.post("/")
async def root():
    return {"message": "Hello, World!"}