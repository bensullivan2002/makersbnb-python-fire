from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User

"""
When I use find I get a user back by their user_id
"""
def test_get_user_back_based_on_id(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    user_repository = UserRepository(db_connection)
    result = user_repository.find(2)
    assert result == User(2, 'angelica@gmail.com', 'Password567!', 'Angelica', 'Gottlieb', '07895687907')



"""
When I use find_user_from_email, I get user back with their information
"""

def test_find_user_from_email(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    user_repository = UserRepository(db_connection)
    user = user_repository.find_user_from_email('angelica@gmail.com')
    assert user == User(2, 'angelica@gmail.com', 'Password567!', 'Angelica', 'Gottlieb', '07895687907')

def test_find_user_from_email_doesnt_exist(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    user_repository = UserRepository(db_connection)
    assert user_repository.find_user_from_email('none@gmail.com') == None
    


"""
When we use login, if username and password match 
"""

"""
When we sign up, a user is added to the database 
"""
def test_sign_up_adds_database(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    user_repository = UserRepository(db_connection)
    user = User(None, 'james@gmail.com', 'Password555!', 'James', 'Rumble', '07895687912')
    user_repository.create(user)
    print(user)
    users = user_repository.all()
    assert users == [User(1, 'ben@gmail.com', 'Password123!', 'Ben', 'Sullivan', '07223487567'), User(2, 'angelica@gmail.com', 'Password567!', 'Angelica', 'Gottlieb', '07895687907'), User(3, 'james@gmail.com', 'Password555!', 'James', 'Rumble', '07895687912')]

