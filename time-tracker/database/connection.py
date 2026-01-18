import sqlite3
def get_connection():
    return sqlite3.connect("timetracker.db")
    
def setup_database(con):
    cursor=con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTs USERS ( ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRSTNAME VARCHAR(20), LASTNAME VARCHAR(20), PASSWORD VARCHAR(20))")
    cursor.execute("CREATE TABLE IF NOT EXISTs TASKS ( ID INTEGER PRIMARY KEY AUTOINCREMENT, TASKNAME VARCHAR(20), DESCRIPTION VARCHAR(100), STARTTIME VARCHAR(20), ENDTIME VARCHAR(20))")
    con.commit()  
    con.close()  
    return cursor

def show_tables():
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")
    con.close()

if __name__ == "__main__":
    con=get_connection()
    show_tables()
    print("Database setup complete")