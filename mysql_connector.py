import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
from click import password_option
def my_connector():
    try:
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="career_db")
        return conn
    except Exception as e:
        print("database connection error",e)
        return None