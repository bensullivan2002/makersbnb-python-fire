class User:
    def __init__(self, id, email, password, first_name, last_name, phone_number, is_logged_on = False):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name 
        self.phone_number = phone_number
        self.is_logged_on = is_logged_on
        self.bookings = []
        self.listings = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.email}, PASSWORD = ***, {self.first_name}, {self.last_name}, {self.phone_number})"





