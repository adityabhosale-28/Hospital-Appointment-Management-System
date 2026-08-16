from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from config import Config
from models.auth import get_user_by_email, verify_password, create_patient, create_doctor
from utils import verify_token

class RegisterRequest(BaseModel):
    role: str
    name: str
    email: str
    password: str
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    blood_grp: Optional[str] = None
    qualification: Optional[str] = None
    specialization: Optional[str] = None
    fee: Optional[float] = None

class LoginRequest(BaseModel):
    email: str
    password: str
    role: str

router = APIRouter()

@router.post('/register')
def register(data: RegisterRequest):
    data_dict = data.dict()
    role = data.role
    
    if role == 'Patient':
        success = create_patient(data_dict)
    elif role == 'Doctor':
        success = create_doctor(data_dict)
    else:
        raise HTTPException(status_code=400, detail="Invalid role for registration")
        
    if success:
        return {"message": f"{role} registered successfully!"}
    else:
        raise HTTPException(status_code=400, detail="Registration failed. Email might already exist.")

@router.post('/login')
def login(data: LoginRequest):
    email = data.email
    password = data.password
    role = data.role

    user = get_user_by_email(email, role)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password, user['Password_Hash']):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if role == 'Doctor' and not user.get('is_approved', False):
         raise HTTPException(status_code=403, detail="Doctor account not verified by Admin.")

    user_id = user[f'{role}_ID']
    expire = datetime.utcnow() + timedelta(hours=24)
    token = jwt.encode(
        {'id': user_id, 'role': role, 'exp': expire},
        Config.SECRET_KEY, algorithm=Config.ALGORITHM
    )

    return {"token": token, "role": role, "user": {"id": user_id, "name": user['Name'], "email": user['Email']}}

@router.get('/me')
def get_me(current_user: dict = Depends(verify_token)):
    return {"user": current_user}
