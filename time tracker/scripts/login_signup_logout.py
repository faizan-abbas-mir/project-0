def signup():
    global firstname,lastname,password
    print("Signup function called")
    firstname=input("Enter first name: ")
    lastname=input("Enter last name: ")
    password=input("Enter password: ")
    print(f"welcome to timetracker {firstname} {lastname}")
    return firstname,lastname,password
    
def login():
    print("please login to your account")
    entredname=input("Enter your first name: ")
    entredpassword=input("Enter your password: ")
    if entredpassword==password and entredname==firstname:
        print("welcome back!")
    else:
        print("who you nigga?")

def is_user(): 
    print("do you have an account?")
    input_value=input("y/n: ")
    if input_value=="n":
        signup()
        login()
    elif input_value=="y":
        login()
        
is_user()