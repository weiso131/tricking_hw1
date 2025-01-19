from . import auth, user

def init_app(db):
    auth.init_app(db)
    auth.init_app(db)