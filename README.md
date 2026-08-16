# Hospital Appointment Management System

## 8️⃣ Step-by-step run guide

### 1️⃣ DATABASE SETUP
Open MySQL and run:
```sql
CREATE DATABASE hospital_db;
USE hospital_db;
SOURCE database/schema.sql;
```

### 2️⃣ BACKEND SETUP
Open a terminal in the `hospital-ams` folder and run:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Backend runs at: `http://127.0.0.1:5000`

### 3️⃣ FRONTEND SETUP
Open **ONLY** the `frontend` folder in VS Code.
Right click on `index.html` → **Open with Live Server**.
Frontend runs at: `http://127.0.0.1:5500`

---

## 9️⃣ Test credentials

**Admin** (Pre-seeded in database):
- Email: `admin@hospital.com`
- Password: `admin123`
- Role: `Admin`

**Doctor / Patient**:
You can register new patients and doctors via the Registration page. 
*Note: Doctors must be verified by the Admin before they can log in!*
