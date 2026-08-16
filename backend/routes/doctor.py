from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from utils import require_role
from models.doctor import get_doctor_today_appointments, add_prescription, add_bill

class PrescriptionRequest(BaseModel):
    appointment_id: int
    diagnosis: str
    medicine: str
    dosage: str

class BillRequest(BaseModel):
    appointment_id: int
    amount: float
    payment_mode: Optional[str] = "Cash"

router = APIRouter()

@router.get('/appointments/today')
def today_appointments(current_user: dict = Depends(require_role('Doctor'))):
    return {"appointments": get_doctor_today_appointments(current_user['id'])}

@router.post('/prescription')
def create_prescription(data: PrescriptionRequest, current_user: dict = Depends(require_role('Doctor'))):
    if add_prescription(data.dict()):
         return {"message": "Prescription added successfully!"}
    raise HTTPException(status_code=500, detail="Failed to add prescription")

@router.post('/bill')
def create_bill(data: BillRequest, current_user: dict = Depends(require_role('Doctor'))):
    if add_bill(data.dict()):
         return {"message": "Bill generated successfully!"}
    raise HTTPException(status_code=500, detail="Failed to generate bill")
