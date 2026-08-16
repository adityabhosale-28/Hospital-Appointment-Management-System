from fastapi import APIRouter, HTTPException, Depends
from utils import require_role
from models.admin import get_all_doctors, verify_doctor_db, get_all_patients, get_all_appointments

router = APIRouter()

@router.get('/doctors')
def list_doctors(current_user: dict = Depends(require_role('Admin'))):
    return {"doctors": get_all_doctors()}

@router.post('/verify-doctor/{doctor_id}')
def verify_doctor(doctor_id: int, current_user: dict = Depends(require_role('Admin'))):
    if verify_doctor_db(doctor_id):
        return {"message": "Doctor verified successfully!"}
    raise HTTPException(status_code=500, detail="Failed to verify doctor")

@router.get('/patients')
def list_patients(current_user: dict = Depends(require_role('Admin'))):
    return {"patients": get_all_patients()}

@router.get('/appointments')
def list_appointments(current_user: dict = Depends(require_role('Admin'))):
    return {"appointments": get_all_appointments()}
