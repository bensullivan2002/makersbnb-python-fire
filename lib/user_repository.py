from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (email, password, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s, %s)', [user.email, user.password, user.first_name, user.last_name, user.phone_number])
        return None 
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user =  User(row["id"], row["email"], row["password"], row["first_name"], row["last_name"], row["phone_number"])
            users.append(user)
        return users
    
    

    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id=%s', [user_id])
        row = rows[0]
        user = User(row["id"], row["email"], row["password"], row["first_name"], row["last_name"], row["phone_number"])
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
        user = User(row["id"], row["email"], row["password"], row["first_name"], row["last_name"], row["phone_number"])
        return user

