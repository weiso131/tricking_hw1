from fastapi import APIRouter
import bcrypt



collection = None

def init_app(db):
    global collection
    collection = db['user']


router = APIRouter()
@router.get("/login")
async def root(account: str, password: str):
    account_key = ["name", "email", "phone"]
    user = None
    for i in range(3):
        find = await collection.find_one({account_key[i]: account})
        if find and bcrypt.checkpw(password.encode(), find["password"]):
            user = find
            break
    if user:
        uid = user["uid"]
        return {"status_code": True,"uid": uid}
    else:
        return {"status_code": False, "message": "Incorrect account or password"}