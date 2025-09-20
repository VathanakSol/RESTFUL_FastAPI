from fastapi import APIRouter, Depends
from core.config import settings
from core.security import get_api_key 

router = APIRouter()

@router.get("/show")
def message(api_key: str = Depends(get_api_key)):
    return {
        "status": "Display Message 🧪"
    }

@router.get("/key")
def get_key(api_key: str = Depends(get_api_key)):
    return {
        "key": settings.api_key
    }

