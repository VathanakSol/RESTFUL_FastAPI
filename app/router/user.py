from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List

from schemas.user import UserCreate, UserUpdate, UserOut, BaseResponse
from crud import user as crud
from api.deps import get_db, get_current_user

router = APIRouter()

# List all users
@router.get("/", response_model=List[UserOut])
def list_users(current_user: UserOut = Depends(get_current_user),db: Session = Depends(get_db)):
    return crud.get_users(db)

# Create user
@router.post("/", response_model=BaseResponse[UserOut])
def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    user_create = crud.create_user(db, user)
    return BaseResponse(message="User Created Successfully ✅", data=user_create)

# Get user via ID
@router.get("/{user_id}", response_model=BaseResponse[UserOut])
def get_user(user_id: int, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return BaseResponse(message="User Founded 🔍", data=db_user)

# Update User via ID
@router.put("/{user_id}", response_model=BaseResponse[UserOut])
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return BaseResponse(message="User Updated Successfully ✅", data=db_user)

# Delete User via ID
@router.delete("/{user_id}", response_model=BaseResponse[UserOut])
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return BaseResponse(message="User Deleted Successfully ✅", data=db_user)





