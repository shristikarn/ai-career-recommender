import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="career_db"
)
cursor=conn.cursor()
#take input
name=input("Enter your name:")
skills=input("Enter your skills(comma separated):")
interests=input("Enter your interests:")
level=input("Enter your level:")
score=float(input("enter your academic score:"))
#clean input
skills=skills.strip()
interests=interests.strip().lower()
level=level.strip().lower()
query=""" INSERT INTO users_input(name,skills,interests,level,academic_score)VALUES(%s,%s,%s,%s,%s)"""
cursor.execute(query,(name,skills,interests,level,score))
conn.commit()
print("user data inserted sucessfully!")
cursor.close()
conn.close()