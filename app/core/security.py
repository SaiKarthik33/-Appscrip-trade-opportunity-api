from fastapi import Header, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.core.config import settings

limiter = Limiter(key_func=get_remote_address)

async def verify_token(x_token: str = Header(...)):
    if x_token != settings.API_SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid Authentication Token")
    return x_token