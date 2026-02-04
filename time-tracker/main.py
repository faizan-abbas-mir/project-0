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
    entered_password= input("enter password: ")
    return entered_firstname,entered_password

login_success=False

while login_success==False:
    user_input=input("do you have an account? y/n \n")
    if user_input=="y":
        print("login function called")
        entered_firstname,entered_password=login()
        if manager.find_user(entered_firstname,entered_password):
            loggedin_user=manager.find_user(entered_firstname,entered_password)
            id=loggedin_user[0]
            print(f"welcome")
            print(id)
            login_success=True
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
            loggedin_user=manager.find_user(entered_firstname,entered_password)
            id=loggedin_user[0]
            print("welcome")
            print(id)
            login_success=True
        else:
            print("no user found")

def new_task():
    taskname=input("what are you working on today?\n")
    print("sounds great... Lets add it to the task\n")
    description=input("enter the task description:\n")
    category=input("enter the task category:\n")
    task=Task(id,taskname,description,category,status="stating")
    input("enter stop to stop duration of task")
    task.stop()
    taskmanager.save_task(task)
    con.commit()
    print(f"task {taskname} started at {task.starttime} and ended at {task.endtime}")

activity=input("enter n for new task and h for history\n")
if activity=="h":
    print(taskmanager.get_user_task(id))
elif activity=="n":
    new_task()




