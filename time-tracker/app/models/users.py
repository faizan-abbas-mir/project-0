#this folder contains user data
import json
class user:
    def __init__(self,firstname,lastname,password):
        self.firstname=firstname
        self.lastname=lastname
        self.password=password
    
    def check_password(self,entered_password):
        return entered_password==self.password
    
    def to_dict(self):
       return {
            "firstname":self.firstname,
            "lastname":self.lastname,
            "password":self.password
        }
class usermanager:
    def __init__(self,filepath,data):
        self.filepath=filepath
        self.data=data

    def save_user(self):
        try:
            with open(self.filepath,"a") as f:
                self.data=json.load(f)
            users=self.data.get("users",[]) 
        except FileNotFoundError:
            users=[]