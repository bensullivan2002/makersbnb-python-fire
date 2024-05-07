from lib.user import User 

def test_formats_nicely():
    test_user = User(1, "angelica@gmail.com", "Password234!", "Angelica", "Gottlieb", "07575888444")
    assert str(test_user) == "User(1, angelica@gmail.com, PASSWORD = ***, Angelica, Gottlieb, 07575888444)"

def test_users_are_equal():
    test_user1 = User(1, "angelica@gmail.com", "Password234!", "Angelica", "Gottlieb", "07575888444")
    test_user2 = User(1, "angelica@gmail.com", "Password234!", "Angelica", "Gottlieb", "07575888444")
    assert test_user1 == test_user2