import pymysql
import json
import datetime

def default_converter(o):
    if isinstance(o, datetime.date):
        return o.isoformat()
    return str(o)

conn = pymysql.connect(host='127.0.0.1', user='root', password='Shyam@2006', database='hospital_db', cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
cursor.execute('SELECT Appointment_ID, Doctor_ID, Date FROM Appointment')
apps = cursor.fetchall()
cursor.execute('SELECT Doctor_ID, Name FROM Doctor')
docs = cursor.fetchall()

print(json.dumps({"appointments": apps, "doctors": docs}, default=default_converter, indent=2))
conn.close()
