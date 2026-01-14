from login_signup_logout import login


def is_logged_in():
    if login:
        return True
    else:
        return False
