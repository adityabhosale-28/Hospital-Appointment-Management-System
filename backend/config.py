import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-hospital-key'
    ALGORITHM = "HS256"
    DB_HOST = os.environ.get('DB_HOST') or '127.0.0.1'
    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'Shyam@2006'
    DB_NAME = os.environ.get('DB_NAME') or 'hospital_db'
