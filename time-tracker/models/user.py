class User:
    def __init__(self, firstname, lastname, password):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def check_password(self, entered_password):
        return self.password == entered_password


class UserManager:
    def __init__(self, con):
        self.con = con

    def save_user(self, user):
        cursor = self.con.cursor()
        cursor.execute(
            "INSERT INTO USERS(FIRSTNAME, LASTNAME, PASSWORD) VALUES(?, ?, ?)",
            (user.firstname, user.lastname, user.password)
        )
        self.con.commit()

    def find_user(self, firstname, password):
        cursor = self.con.cursor()
        cursor.execute(
            "SELECT * FROM USERS WHERE FIRSTNAME=? AND PASSWORD=?",
            (firstname, password)
        )
        return cursor.fetchone()

    def list_all_users(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM USERS")
        return cursor.fetchall()
    