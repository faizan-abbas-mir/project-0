"this file contains the Task model for the time-tracker application"
from database.connection import get_connection
con = get_connection()
from datetime import datetime

class Task:
    def __init__(self,user_id,taskname,taskdescription,status):
        self.user_id=user_id
        self.taskname=taskname
        self.taskdescription=taskdescription
        self.starttime=datetime.now()
        self.endtime=None
        self.status=status

    def stop(self):
        self.endtime=datetime.now()
    
    def get_duration(self):
        "gets the duration of task"
        if self.endtime is None:
            return None
        else:
            duration=self.endtime-self.starttime
            return duration.total_seconds()
        
    def to_dict(self):
        return {
            "user_id":self.user_id,
            "taskname":self.taskname,
            "description":self.taskdescription,
            "starttime":self.starttime.strftime("%Y-%m-%d %H:%M:%S"),
            "entime":self.endtime.strftime("%Y-%m-%d %H:%M:%S") if self.endtime else None
             }
    
class TaskManager:
    def __init__(self,con):
        self.con=con

    def save_task(self,task):
        cursor=self.con.cursor()
        cursor.execute("INSERT INTO TASKS(USER_ID,TASKNAME,DESCRIPTION,STARTTIME,ENDTIME,STATUS) VALUES(?,?,?,?,?,?)",
                        (task.user_id,task.taskname,task.taskdescription,task.starttime.strftime("%Y-%m-%d %H:%M:%S"),task.endtime.strftime("%Y-%m-%d %H:%M:%S") if task.endtime else None,task.status))
        con.commit()
        
    def get_user_task(self,user_id):
        cursor=self.con.cursor()
        cursor.execute("SELECT taskname,description,starttime,endtime,status FROM TASKS WHERE USER_ID=?", (user_id,))
        rows=cursor.fetchall()
        user_tasks=[]
        for row in rows:
            user_tasks.append(row)
        return user_tasks

