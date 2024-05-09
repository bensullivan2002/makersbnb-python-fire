from lib.space import Space 

def test_formats_nicely():
    test_space = Space(1, "Jungle Paradise", "1 bed luxury apartment!", 200, 3)
    assert str(test_space) == "Space(1, Jungle Paradise, 1 bed luxury apartment!, 200, 3)"

def test_users_are_equal():
    test_space1 = Space(1, "Jungle Paradise", "1 bed luxury apartment!", 200, 3)
    test_space2 = Space(1, "Jungle Paradise", "1 bed luxury apartment!", 200, 3)
    assert test_space1 == test_space2