import sqlite3
from .user import User, UserManager

# Connect to database
con = sqlite3.connect("timetracker.db")
cursor = con.cursor()

# Create manager
manager = UserManager(cursor)

# Test save
user = User("John", "Doe", "pass123")
manager.save_user(user)
print("User saved!")

# Test find
found = manager.find_user("John","pass123")
if found:
    print(f"Found: {found}")
else:
    print("Not found")

#con.close()