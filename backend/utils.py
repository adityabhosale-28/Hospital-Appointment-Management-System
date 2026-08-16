from fastapi import Request, HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from config import Config

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        return {"id": payload.get("id"), "role": payload.get("role")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

def require_role(role: str):
    def role_checker(user: dict = Depends(verify_token)):
        if user.get("role") != role:
            raise HTTPException(status_code=403, detail="Unauthorized role!")
        return user
    return role_checker
