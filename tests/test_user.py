from lib.user import User

"""
As a user, when I create a User class, it constructs a User
with an email, password, and user_id and is_logged_on == false
"""

def test_user_innit():
    example = User(1, 'example@hotmail.com', 'Examplepassword123', False)
    assert example.id == 1
    assert example.email == 'example@hotmail.com'
    assert example.password == 'Examplepassword123'
    assert example.is_logged_on == False

"""
User objects in different classes are treated as equals
"""

def test_user_obects_are_equal():
    example1 = User(1, 'example@hotmail.com', 'Examplepassword123', False)
    example2 = User(1, 'example@hotmail.com', 'Examplepassword123', False)
    assert example1 == example2

"""
Returns user objects as nice strings
"""

def test_objects_returned_as_formatted_strings():
    example = User(1, 'example@hotmail.com', 'Examplepassword123')
    assert str(example) == "User(1, example@hotmail.com, Examplepassword123)"
