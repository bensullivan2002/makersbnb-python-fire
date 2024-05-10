from utils.validate_email import *
from utils.validate_phone_number import *
from utils.validate_password import *


class User:
    def __init__(self, id, email, password, first_name, last_name, phone_number, is_logged_on=False):
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

    def generate_errors(self):
        errors = []
        if not is_valid_email(self.email):
            errors.append("Invalid email format")
        if not is_valid_uk_phone_number(self.phone_number):
            errors.append("Invalid phone number")
        if not is_valid_password(self.password):
            errors.append(
                "Invalid password. Password must be at least 8 characters, contain one uppercase character and at "
                "least one special character")
        return errors

        # Worked generate errors functionality on 8 May afternoon
