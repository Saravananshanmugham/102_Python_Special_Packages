import sqlite3  
  
con = sqlite3.connect("IR40.db")  
print("Database opened successfully")  
create_table = """ create table student_record (
    Enr_no INTEGER PRIMARY KEY,
    Stud_name TEXT NOT NULL,
    passwd TEXT NOT NULL
)
"""
  
con.execute(create_table)  
  
print("Table created successfully")  
  
con.close()  