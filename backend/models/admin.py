from db import get_db_connection

def get_all_doctors():
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    cursor.execute("SELECT Doctor_ID, Name, Qualification, Specialization, Fee, Email, is_approved FROM Doctor")
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def verify_doctor_db(doctor_id):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Doctor SET is_approved = TRUE WHERE Doctor_ID = %s", (doctor_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_all_patients():
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    cursor.execute("SELECT Patient_ID, Name, Age, Gender, Phone, Blood_Grp, Email FROM Patient")
    patients = cursor.fetchall()
    conn.close()
    return patients

def get_all_appointments():
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    query = """
        SELECT a.Appointment_ID, a.Date, a.Time, a.Token_No, a.Status, a.Problem,
               p.Name as Patient_Name, d.Name as Doctor_Name
        FROM Appointment a
        LEFT JOIN Patient p ON a.Patient_ID = p.Patient_ID
        LEFT JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
        ORDER BY a.Date DESC, a.Time DESC
    """
    cursor.execute(query)
    apps = cursor.fetchall()
    for app in apps:
        if 'Date' in app and hasattr(app['Date'], 'isoformat'):
            app['Date'] = app['Date'].isoformat()
        if 'Time' in app and hasattr(app['Time'], 'total_seconds'):
            app['Time'] = str(app['Time'])
    conn.close()
    return apps
