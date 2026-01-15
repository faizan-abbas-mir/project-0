import json
#from scripts.login_signup_logout import firstname, lastname, password
 
file_path="app/data/data.json"
def save_user_data(firstname, lastname, password ):
    try:
        with open(file_path,"a") as f:
            data=json.load(f)
            users=data.get("users",[]) 
    except FileNotFoundError:
        users=[]
    new_user= {
        "firstname":firstname,
        "lastname":lastname,
        "password":password
        }
    users.append(new_user)
    with open(file_path,"w") as f:
        json.dump({"users":users},f,index=2)

def load_user_data():
    try:
        with open(file_path, "r")as f:
            data=json.load(f)
            users=data.get(users)
        for users in users:
            if user[firstname]==firstname:
                return user
    except FileNotFoundError:
        return None