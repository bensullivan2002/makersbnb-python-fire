from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User

"""
When I use find I get a user back by their user_id
"""
def test_get_user_back_based_on_id(db_connection):
    db_connection.seed('seeds/user_library.sql')
    user_repository = UserRepository(db_connection)
    result = user_repository.find(2)
    assert result == User(2, 'example2@hotmail.com', 'Password12345')

"""
When I use check_email_valid I get True if email already exists
"""
def test_get_user_back_based_on_email(db_connection):
    db_connection.seed('seeds/user_library.sql')
    user_repository = UserRepository(db_connection)
    result = user_repository.check_email_valid('example2@hotmail.com')
    result2 = user_repository.check_email_valid('wrongemail@hotmail.com')
    assert result == True
    assert result2 == False

"""
When I use find_user_from_email, I get user back with their information
"""

def test_find_user_from_email(db_connection):
    db_connection.seed('seeds/user_library.sql')
    user_repository = UserRepository(db_connection)
    user = user_repository.find_user_from_email('example2@hotmail.com')
    assert user == User(2, 'example2@hotmail.com', 'Password12345')

"""
When we use login, if username and password match 
"""


# """
# When I use check_password_matches_email I get True if password matches email
# """

# def test_password_matches_email(db_connection):
#     db_connection.seed('seeds/user_library.sql')
#     user_repository = UserRepository(db_connection)
#     password_matches = user_repository.check_password_matches_email('example2@hotmail.com', 'Password12345')
#     assert password_matches == True