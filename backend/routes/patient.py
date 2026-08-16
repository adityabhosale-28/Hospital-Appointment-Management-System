from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from utils import require_role
from models.patient import get_verified_doctors, book_appointment, get_patient_appointments, get_patient_appointment_details, pay_bill

class BookRequest(BaseModel):
    doctor_id: int
    date: str
    time: str
    problem: Optional[str] = None

class PayBillRequest(BaseModel):
    payment_mode: str

router = APIRouter()

@router.get('/doctors')
def list_doctors(current_user: dict = Depends(require_role('Patient'))):
    return {"doctors": get_verified_doctors()}

@router.post('/book')
def book(data: BookRequest, current_user: dict = Depends(require_role('Patient'))):
    data_dict = data.dict()
    data_dict['patient_id'] = current_user['id']
    if book_appointment(data_dict):
        return {"message": "Appointment booked successfully!"}
    raise HTTPException(status_code=500, detail="Failed to book appointment")

@router.get('/appointments')
def get_appointments(current_user: dict = Depends(require_role('Patient'))):
    apps = get_patient_appointments(current_user['id'])
    return {"appointments": apps}

@router.get('/appointment/{app_id}/details')
def get_appointment_details(app_id: int, current_user: dict = Depends(require_role('Patient'))):
    details = get_patient_appointment_details(app_id, current_user['id'])
    if not details: raise HTTPException(status_code=404, detail="Details not found")
    return details

@router.post('/pay-bill/{app_id}')
def pay_appointment_bill(app_id: int, data: PayBillRequest, current_user: dict = Depends(require_role('Patient'))):
    if pay_bill(app_id, current_user['id'], data.payment_mode):
        return {"message": f"Bill paid successfully via {data.payment_mode}"}
    raise HTTPException(status_code=500, detail="Payment failed. Appointment may not belong to you.")
