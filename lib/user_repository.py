from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id=%s', [user_id])
        row = rows[0]
        user = User(row["id"], row["email"], row["password"])
        return user
    
    def check_email_valid(self, user_email):
        rows = self._connection.execute('SELECT * FROM users WHERE email=%s', [user_email])
        if len(rows) == 0:
            return False
        else:
            return True
        
    def find_user_from_email(self, user_email):
        rows = self._connection.execute('SELECT * FROM users WHERE email=%s', [user_email])
        row = rows[0]
        user = User(row["id"], row["email"], row["password"])
        return user

    # def check_password_matches_email(self, user_email, user_password):
    #     if self.check_email_valid(user_email) == True:
    #         self.find()
    #     rows = self._connection.execute('SELECT ')