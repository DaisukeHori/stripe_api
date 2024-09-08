from fastapi import Header, HTTPException
from app.core.config import settings

async def verify_auth_key(x_auth_key: str = Header(...)):
    if x_auth_key != settings.AUTH_KEY:
        raise HTTPException(status_code=401, detail="Invalid authentication key")
    return x_auth_key
