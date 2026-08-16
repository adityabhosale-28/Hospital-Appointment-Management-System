from db import get_db_connection
import datetime

def get_doctor_today_appointments(doctor_id):
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    today = datetime.date.today()
    query = """
        SELECT a.Appointment_ID, a.Time, a.Date, a.Token_No, a.Status, a.Problem, p.Name as Patient_Name, p.Age, p.Gender, p.Phone
        FROM Appointment a
        JOIN Patient p ON a.Patient_ID = p.Patient_ID
        WHERE a.Doctor_ID = %s
        ORDER BY a.Date ASC, a.Token_No ASC
    """
    cursor.execute(query, (doctor_id,))
    apps = cursor.fetchall()
    for app in apps:
        if 'Date' in app and hasattr(app['Date'], 'isoformat'):
            app['Date'] = app['Date'].isoformat()
        if 'Time' in app and hasattr(app['Time'], 'total_seconds'):
            app['Time'] = str(app['Time'])
    conn.close()
    return apps

def add_prescription(data):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        query = """INSERT INTO Prescription (Appointment_ID, Diagnosis, Medicine, Dosage)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (
            data['appointment_id'], data['diagnosis'], 
            data['medicine'], data['dosage']
        ))
        # Update appointment status to Completed
        cursor.execute("UPDATE Appointment SET Status = 'Completed' WHERE Appointment_ID = %s", (data['appointment_id'],))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def add_bill(data):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        today = datetime.date.today()
        query = """INSERT INTO Bill (Appointment_ID, Bill_Date, Amount, Payment_Mode, Payment_Status)
                   VALUES (%s, %s, %s, %s, 'Unpaid')"""
        cursor.execute(query, (
            data['appointment_id'], today, data['amount'], data.get('payment_mode', 'Cash')
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()
