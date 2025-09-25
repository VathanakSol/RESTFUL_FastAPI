from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from schemas.user import UserCreate, UserOut, Token
from crud import user as crud
from api.deps import get_db, get_current_user
from core.security import get_password_hash, verify_password, create_access_token
from core.config import settings

router = APIRouter()

# Register Route
@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if username already exists
        if crud.get_user_by_username(db, user.username):
            raise HTTPException(status_code=400, detail="Username already registered")
        
        # Check if email already exists
        if crud.get_user_by_email(db, user.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Hash password and create user
        hashed_password = get_password_hash(user.password)
        created_user = crud.create_user(db, user, hashed_password)
        
        if not created_user:
            raise HTTPException(status_code=500, detail="Failed to create user")
            
        return created_user
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")

# Login Route (Token)
@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.username, expires_delta=access_token_expires)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Protected Route
@router.get("/me", response_model=UserOut)
def get_me(current_user: UserOut = Depends(get_current_user)):
    return current_user 
