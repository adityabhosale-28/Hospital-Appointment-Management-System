import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, patient, doctor, admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api", tags=["Auth"])
app.include_router(patient.router, prefix="/api/patient", tags=["Patient"])
app.include_router(doctor.router, prefix="/api/doctor", tags=["Doctor"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Hospital AMS API is running on FastAPI!"}

if __name__ == "__main__":
    # Start auto-reloading Uvicorn server on port 8000
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
