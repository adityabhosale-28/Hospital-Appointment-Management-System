import pymysql
from config import Config

def get_db_connection():
    try:
        connection = pymysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.Error as err:
        print(f"Database Error: {err}")
        return None
