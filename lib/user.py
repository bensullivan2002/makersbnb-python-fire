class User:
    def __init__(self, id, email, password, is_logged_on = False):
        self.id = id
        self.email = email
        self.password = password
        self.is_logged_on = is_logged_on

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.password})"