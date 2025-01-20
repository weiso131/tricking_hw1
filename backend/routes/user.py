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


    return {"status_code": True}

@router.get("/get")
async def get_user(uid: str):
    user = await collection.find_one({"uid" : uid})
    
    if user:
        user.pop("_id", None)
        return User(**user)
    else:
        return HTTPEXCEPTION_USER_NOT_EXIST

@router.post("/update")
async def update_user(data: UserUpdate):
    user = await collection.find_one({"uid" : data.uid})
    if user:
        update_data = {k: v for k, v in data.model_dump().items() if v is not None}

        await collection.update_one(
            {"uid": data.uid},
            {"$set": update_data}
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
    