import sqlite3

con=sqlite3.connect("timetracker.db")
cursor=con.cursor()

"""def create_database():
    cursor.execute("CREATE DATABASE TIMETRACKER:")"""

def create_user_table():
    cursor.execute("CREATE TABLE IF NOT EXISTs USER ( ID INTEGER UNIQUE, FIRSTNAME VARCHAR(20), LASTNAME VARCHAR(20), PASSWORD VARCHAR(20))")

def create_task_table():
    cursor.execute("CREATE TABLE IF NOT EXISTs TASK ( ID INTEGER UNIQUE, TASKNAME VARCHAR(20), DESCRIPTION VARCHAR(100), STARTTIME VARCHAR(20), ENDTIME VARCHAR(20))")

def show_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")


create_task_table()
create_user_table()
show_tables()
con.commit()
con.close()
print("Database setup complete")