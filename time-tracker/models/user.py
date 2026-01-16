from database.connection import con
cursor=con.cursor()
class User:
    def __init__(self,firstname,lastname,password):
        self.firstname=firstname
        self.lastname=lastname
        self.password=password
    
    def check_password(self,entered_password):
        return self.password==entered_password
    
class UserManager:
    def __init__(self,cursor):
        self.cursor=cursor

    def save_user(self,user):
        self.cursor.execute("INSERT INTO USERS(FIRSTNAME,LASTNAME,PASSWORD) VALUES(?,?,?)",
                       (user.firstname,user.lastname,user.password))
        con.commit()
        
    def find_user(self,firstname):
        self.cursor.execute("SELECT * FROM USERS WHERE FIRSTNAME=?",firstname)
        return self.cursor.fetchone
    