from .task import TaskManager,Task
from  database.connection import get_connection, setup_database
import time

con=get_connection()
setup_database(con)

taskmanager=TaskManager(con)
print("creating a task")
task=Task(2,"breakfast","eating","to-do")
taskmanager.save_task(task)
con.commit()
user_task=taskmanager.get_user_task(2)
print(user_task)
