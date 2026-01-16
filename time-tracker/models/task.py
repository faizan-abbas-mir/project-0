"this file contains the Task model for the time-tracker application"
from database.connection import con
cursor=con.cursor()

class Tasks:
    def __init__(self,id,taskname,taskdescription,starttime,endtime,status):
        self.id=id
        self.taskname=taskname
        self.taskdescription=taskdescription
        self.starttime=starttime
        self.endtime=endtime
        self.status=status

    def enter_task(self,con):
        cursor.execute("INSERT INTO TASK ( ID,TASKNAME,DESCRIPTION,STARTIME,ENDTIME,STATUS) VALUES(?,?,?,?,?)",
                       (self.id,self.taskname,self.taskdescription,self.starttime,self.endtime,self.status))
        con.commit()


