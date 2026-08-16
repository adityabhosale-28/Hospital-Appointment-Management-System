# 🏥 Hospital Appointment Management System

A full-stack **Hospital Appointment Management System (HAMS)** designed to simplify hospital operations by providing a centralized platform for managing patients, doctors, appointments, prescriptions, and billing.

The system supports **role-based access** for Admin, Doctor, and Patient users and uses a Flask backend with a MySQL database.

---

## 🚀 Getting Started

Follow the steps below to set up and run the project locally.

### 1️⃣ Database Setup

Make sure **MySQL Server** is installed and running.

Open MySQL and execute the following commands:

```sql
CREATE DATABASE hospital_db;
USE hospital_db;
SOURCE database/schema.sql;
```

This will create the `hospital_db` database and initialize the required tables and database structure.

---

### 2️⃣ Backend Setup

Open a terminal in the root `hospital-ams` project directory.

Navigate to the backend folder:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask backend:

```bash
python app.py
```

The backend server will be available at:

```text
http://127.0.0.1:5000
```

> **Note:** Keep the backend terminal running while using the application.

---

### 3️⃣ Frontend Setup

For the frontend, open **only the `frontend` folder** in Visual Studio Code.

1. Open `index.html`.
2. Right-click on `index.html`.
3. Select **Open with Live Server**.
4. The application will open in your browser.

The frontend will be available at:

```text
http://127.0.0.1:5500
```

> **Important:** Make sure the Flask backend is running before accessing the frontend.

---

# 🔐 Test Credentials

## 👨‍💼 Admin Account

A default Admin account is pre-seeded in the database.

| Field        | Details              |
| ------------ | -------------------- |
| **Email**    | `admin@hospital.com` |
| **Password** | `admin123`           |
| **Role**     | `Admin`              |

The Admin can manage doctors, patients, appointments, and other administrative operations.

---

## 👨‍⚕️ Doctor & 🧑‍💻 Patient Accounts

Doctors and patients can create accounts through the **Registration** page.

### Doctor Verification

> ⚠️ **Important:** Newly registered doctors must be verified by an Admin before they can log in and access the Doctor Dashboard.

Patients can register and access the system without the doctor verification process.

---

# 🛠️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Database:** MySQL
* **API:** REST API
* **Development Environment:** Visual Studio Code
* **Frontend Development Server:** Live Server

---

# 📌 Application URLs

| Component    | URL                     |
| ------------ | ----------------------- |
| **Backend**  | `http://127.0.0.1:5000` |
| **Frontend** | `http://127.0.0.1:5500` |

---

# ⚠️ Security Note

The Admin credentials shown above are intended **only for local development and testing**.

For production deployment, use a strong password and store sensitive credentials securely using environment variables or a dedicated secrets-management solution.

---

## 👨‍💻 Project

**Hospital Appointment Management System (HAMS)**
A DBMS and full-stack web development project demonstrating practical implementation of relational database management, backend APIs, authentication, and role-based access control.

⭐ **If you find this project useful, consider giving the repository a star!**
