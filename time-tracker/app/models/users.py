#this folder contains user data
import json
class User:
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
class UserManager:
    def __init__(self,filepath):
        self.filepath=filepath
        

    def save_user(self,user):
        try:
            with open(self.filepath,"r") as f:
                data=json.load(f)
            users=data.get("users",[]) 
        except FileNotFoundError:
            users=[]
        users.append(user.to_dict())

        with open(self.filepath,"w") as f:
            json.dump({"users":users},f,indent=2)
        
    def find_user(self,firstname):
        try:
            with open(self.filename,"r") as f:
                data=json.load(f)
            users=data.get("users",[])
            for user in users:
                if user["firstname"]==firstname:
                    return User(
                        user["firstname"],
                        user["lastname"],
                        user["password"]
                    )
            return None
        except FileNotFoundError:
            return None

