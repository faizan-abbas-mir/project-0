import sqlite3
from database.connection import get_connection,setup_database
from models.user import User,UserManager

con=get_connection()
setup_database()

def signup():
    firstname=input("enter firstname: ")
    lastname=input("enter lastname: ")
    password= input("enter password: ")
    return firstname,lastname,password

manager=UserManager(con)

def login():
    entered_firstname=input("enter firstname: ")
    entered_password= input("enter password: ")
    return entered_firstname,entered_password

user_input=input("doyou have an account? y/n \n")
if user_input=="y":
    print("login function called")
    entered_firstname,entered_password=login()
    if manager.find_user(entered_firstname,entered_password):
        print("welcome")
    else:
        print("no user found")
    
elif user_input=="n":
    print("signup function called")
    firstname,lastname,password=signup()
    user=User(firstname,lastname,password)
    manager.save_user(user)
    print("login function called")
    entered_firstname,entered_password=login()
    if manager.find_user(entered_firstname,entered_password):
        print("welcome")
    else:
        print("no user found")

con.close()

