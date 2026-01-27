import sqlite3
from database.connection import get_connection,setup_database
from models.user import User,UserManager
from models.task import Task,TaskManager

con=get_connection()
setup_database(con)
cursor=con.cursor()
manager=UserManager(cursor)
taskmanager=TaskManager(con)


def signup():
    firstname=input("enter firstname: ")
    lastname=input("enter lastname: ")
    password= input("enter password: ")
    return firstname,lastname,password

def login():
    entered_firstname=input("enter firstname: ")
    id=input("enter your user id:\n")
    entered_password= input("enter password: ")
    return entered_firstname,id,entered_password

user_input=input("do you have an account? y/n \n")
if user_input=="y":
    print("login function called")
    id,entered_firstname,entered_password=login()
    if manager.find_user(entered_firstname,entered_password):
        print(f"welcome")
    else:
        print("no user found")
    
elif user_input=="n":
    print("signup function called")
    firstname,lastname,password=signup()
    user=User(firstname,lastname,password)
    manager.save_user(user)
    print(f"User saved! All users: {manager.list_all_users()}")
    con.commit()
    print("login function called")
    entered_firstname,entered_password=login()
    if manager.find_user(entered_firstname,entered_password):
        print("welcome")
    else:
        print("no user found")



taskmanager.get_user_task(id)

def new_task():
    taskname=input("what are you working on today?\n")
    print("sounds great... Lets add it to the task\n")
    description=input("enter the task description:\n")
    task=Task(id,taskname,description,status="stating")
    taskmanager.save_task(task)
    con.commit()
    print(f"task {taskname} started at {task.starttime}")
activity=input("enter n for new task and h for history\n")
if activity=="h":
    print(taskmanager.get_user_task(id))
elif activity=="n":
    new_task()

##import the id from login function and pass it to task function