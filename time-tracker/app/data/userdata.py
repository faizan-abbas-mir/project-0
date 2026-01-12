import json
from scripts.login_signup_logout import firstname, lastname, password
 
def save_user_data(firstname, lastname, password ):
    user_data={ 
        "firstname": firstname, 
        "lastname": lastname,
        "password": password
          }
    file_path="app/data/data.json"
    with open(file_path,"w") as f:
        json.dump(user_data,f) 
