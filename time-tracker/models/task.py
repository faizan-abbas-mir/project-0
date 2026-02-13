from datetime import datetime


class Task:
    def __init__(self, user_id, taskname, taskdescription, category, status):
        self.user_id = user_id
        self.taskname = taskname
        self.taskdescription = taskdescription
        self.category = category
        self.starttime = datetime.now()
        self.endtime = None
        self.status = status

    def stop(self):
        self.endtime = datetime.now()
        self.status = "completed"

    def get_duration(self):
        if self.endtime is None:
            return None
        duration = self.endtime - self.starttime
        return duration.total_seconds()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "taskname": self.taskname,
            "description": self.taskdescription,
            "category": self.category,
            "starttime": self.starttime.strftime("%Y-%m-%d %H:%M:%S"),
            "endtime": self.endtime.strftime("%Y-%m-%d %H:%M:%S") if self.endtime else None,
            "status": self.status
        }


class TaskManager:
    def __init__(self, con):
        self.con = con

    def save_task(self, task):
        cursor = self.con.cursor()
        cursor.execute(
            "INSERT INTO TASKS(USER_ID, TASKNAME, DESCRIPTION, CATEGORY, STARTTIME, ENDTIME, STATUS) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (
                task.user_id,
                task.taskname,
                task.taskdescription,
                task.category,
                task.starttime.strftime("%Y-%m-%d %H:%M:%S"),
                task.endtime.strftime("%Y-%m-%d %H:%M:%S") if task.endtime else None,
                task.status
            )
        )
        self.con.commit()

    def get_user_tasks(self, user_id):
        cursor = self.con.cursor()
        cursor.execute(
            "SELECT taskname, description, category, starttime, endtime, status FROM TASKS WHERE USER_ID=?",
            (user_id,)
        )
        return cursor.fetchall()

