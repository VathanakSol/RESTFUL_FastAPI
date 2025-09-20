from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List

from schemas.user import UserCreate, UserUpdate, UserOut
from crud import user as crud
from api.deps import get_db
from core.security import get_api_key
router = APIRouter()

# List all users
@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    return crud.get_users(db)

# Create user
@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    return crud.create_user(db, user)

# Get user via ID
@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user

# Update User via ID
@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user

# Delete User via ID
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return {
        "message": "User has deleted ✅"
    }





