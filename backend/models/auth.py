from db import get_db_connection
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_by_email(email: str, role: str):
    conn = get_db_connection()
    if not conn: return None
    cursor = conn.cursor()
    table = role.capitalize()
    if table not in ['Patient', 'Doctor', 'Admin']: return None
    
    query = f"SELECT * FROM {table} WHERE Email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_patient(data: dict):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    hashed_password = hash_password(data['password'])
    try:
        query = """INSERT INTO Patient (Name, Age, Gender, Phone, Blood_Grp, Email, Password_Hash) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (
            data.get('name'), data.get('age'), data.get('gender'), 
            data.get('phone'), data.get('blood_grp'), 
            data.get('email'), hashed_password
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def create_doctor(data: dict):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    hashed_password = hash_password(data['password'])
    try:
        query = """INSERT INTO Doctor (Name, Qualification, Specialization, Fee, Email, Password_Hash, is_approved) 
                   VALUES (%s, %s, %s, %s, %s, %s, FALSE)"""
        cursor.execute(query, (
            data.get('name'), data.get('qualification'), data.get('specialization'), 
            data.get('fee', 0.0), data.get('email'), hashed_password
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def verify_password(plain_password, hashed_password):
    return hash_password(plain_password) == hashed_password
