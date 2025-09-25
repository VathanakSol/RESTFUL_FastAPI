from sqlalchemy.orm import Session
from db.session import SessionLocal
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from core.security import get_api_key, decode_access_token
from schemas.user import TokenData
from crud import user as crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

def get_current_api_key():
    return Depends(get_api_key)  

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(sub=username)
    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_username(db, username=token_data.sub)
    if user is None:
        raise credentials_exception
    return user


