from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

from core.config import settings

api_key_header = APIKeyHeader(name="X-API-KEY")

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key