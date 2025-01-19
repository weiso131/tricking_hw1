from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserUpdate, User
import bcrypt
import uuid

HTTPEXCEPTION_USER_NOT_EXIST = HTTPException(404, "User not found")


collection = None
def init_app(db):
    global collection
    collection = db['user']


router = APIRouter()

@router.post("/create")
async def create_user(data: UserCreate):
    hashpw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
    uid = str(uuid.uuid4())
    user = {
        "uid": uid,
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "sex": data.sex,
        "age": data.age,
        "password": hashpw,
    }
    await collection.insert_one(user)


    return User(**user)

@router.get("/get")
async def get_user(uid: str):
    user = await collection.find_one({"uid" : uid})
    if user:
        return user
    else:
        return HTTPEXCEPTION_USER_NOT_EXIST

@router.post("/update")
async def update_user(data: UserUpdate):
    user = await collection.find_one({"uid" : data.uid})
    if user:
        await collection.update_one(
            {"uid": data.uid},
            {"$set": data}
        )
        return {"status_code": True}
    else:
        return HTTPEXCEPTION_USER_NOT_EXIST
    
@router.delete("/delete")
async def delete_user(uid: str):
    user = await collection.find_one({"uid" : uid})
    if user:
        await collection.delete_one({"uid": uid})
        return {"message": "create"}
    else:
        return HTTPEXCEPTION_USER_NOT_EXIST
    