import sqlite3


def get_connection():
    return sqlite3.connect("timetracker.db")


def setup_database(con):
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FIRSTNAME VARCHAR(20),
            LASTNAME VARCHAR(20),
            PASSWORD VARCHAR(20)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TASKS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USER_ID INTEGER NOT NULL,
            TASKNAME TEXT NOT NULL,
            DESCRIPTION TEXT,
            CATEGORY TEXT,
            STARTTIME TEXT NOT NULL,
            ENDTIME TEXT,
            STATUS TEXT,
            FOREIGN KEY (USER_ID) REFERENCES USERS(ID)
        )
    """)
    con.commit()


def show_tables():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")
    con.close()


if __name__ == "__main__":
    con = get_connection()
    setup_database(con)
    show_tables()
    print("Database setup complete")