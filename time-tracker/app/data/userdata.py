import json
#from scripts.login_signup_logout import firstname, lastname, password
 
file_path="app/data/data.json"
def save_user_data(firstname, lastname, password ):
    user_data={ 
        "firstname": firstname, 
        "lastname": lastname,
        "password": password
          }
    
    with open(file_path,"w") as f:
        json.dump(user_data,f) 

def load_user_data():
    try:
        with open(file_path, "r")as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("User data not found")
        return None