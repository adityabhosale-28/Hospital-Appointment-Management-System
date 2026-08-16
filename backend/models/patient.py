from db import get_db_connection

def get_verified_doctors():
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    cursor.execute("SELECT Doctor_ID, Name, Qualification, Specialization, Fee FROM Doctor WHERE is_approved = TRUE")
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def book_appointment(data):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        query = """INSERT INTO Appointment (Patient_ID, Doctor_ID, Date, Time, Token_No, Problem)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        # A simple token number logic (e.g. counting today's appointments for that doctor + 1)
        cursor.execute("SELECT COUNT(*) as count FROM Appointment WHERE Doctor_ID = %s AND Date = %s", (data['doctor_id'], data['date']))
        res = cursor.fetchone()
        # Ensure res is not None before indexing
        count = res['count'] if type(res) is dict else (res[0] if res else 0)
        token_no = count + 1
        
        cursor.execute(query, (
            data['patient_id'], data['doctor_id'], data['date'], 
            data['time'], token_no, data['problem']
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_patient_appointments(patient_id):
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor()
    query = """
        SELECT a.Appointment_ID, a.Date, a.Time, a.Token_No, a.Status, a.Problem, d.Name as Doctor_Name
        FROM Appointment a
        JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
        WHERE a.Patient_ID = %s
        ORDER BY a.Date DESC, a.Time DESC
    """
    cursor.execute(query, (patient_id,))
    apps = cursor.fetchall()
    for app in apps:
        if 'Date' in app and hasattr(app['Date'], 'isoformat'):
            app['Date'] = app['Date'].isoformat()
        if 'Time' in app and hasattr(app['Time'], 'total_seconds'):
            app['Time'] = str(app['Time'])
    conn.close()
    return apps

def get_patient_appointment_details(app_id, patient_id):
    conn = get_db_connection()
    if not conn: return None
    cursor = conn.cursor()
    cursor.execute("SELECT Appointment_ID FROM Appointment WHERE Appointment_ID = %s AND Patient_ID = %s", (app_id, patient_id))
    if not cursor.fetchone(): return None
    
    cursor.execute("SELECT * FROM Prescription WHERE Appointment_ID = %s", (app_id,))
    prescription = cursor.fetchone()
    cursor.execute("SELECT * FROM Bill WHERE Appointment_ID = %s", (app_id,))
    bill = cursor.fetchone()
    
    if bill and 'Bill_Date' in bill and hasattr(bill['Bill_Date'], 'isoformat'):
        bill['Bill_Date'] = bill['Bill_Date'].isoformat()
    conn.close()
    return {"prescription": prescription, "bill": bill}

def pay_bill(app_id, patient_id, payment_mode):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    try:
        # verify
        cursor.execute("SELECT Appointment_ID FROM Appointment WHERE Appointment_ID = %s AND Patient_ID = %s", (app_id, patient_id))
        if not cursor.fetchone(): return False
        
        cursor.execute("UPDATE Bill SET Payment_Status = 'Paid', Payment_Mode = %s WHERE Appointment_ID = %s", (payment_mode, app_id))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Payment Error:", e)
        return False
    finally:
        conn.close()

