from app.data.userdata import save_user_data, load_user_data

def signup():
    global firstname,lastname,password
    print("Signup function called")
    firstname=input("Enter first name: ")
    lastname=input("Enter last name: ")
    password=input("Enter password: ")
    print(f"welcome to timetracker {firstname} {lastname}")
    save_user_data(firstname, lastname, password)
    return firstname,lastname,password
    
def login():
    print("please login to your account")
    entredname=input("Enter your first name: ")
    entredpassword=input("Enter your password: ")
    data=load_user_data()
    if entredpassword==data["password"] and entredname==data["firstname"]:
        print("welcome back!")
        return True
    elif data is None:
        print("No user data found. Please sign up first.")
        return False
    else:
        print("who you?")
        return False
    
def is_user(): 
    print("do you have an account?")
    input_value=input("y/n: ")
    if input_value=="n":
        signup()
        login()
    elif input_value=="y":
        login()

is_user()
