from db.session import SessionLocal
from fastapi import Depends 
from core.security import get_api_key

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

def get_current_api_key():
    return Depends(get_api_key)  

