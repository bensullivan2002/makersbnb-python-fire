from lib.space_repository import SpaceRepository
from lib.space import Space

def test_return_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    space_repository = SpaceRepository(db_connection)
    assert space_repository.all() == [
        Space(1, 'Treehouse', '1 bed unique stay', 150, 1),
        Space(2, 'Ocean Apartment', 'Luxury stay by the sea', 200, 2)
    ]

def test_create_space(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    space_repository = SpaceRepository(db_connection)
    space =  Space(None, 'Alehouse', 'free beer', 250, 1)
    space_repository.create(space)
    assert space_repository.all() == [
        Space(1, 'Treehouse', '1 bed unique stay', 150, 1),
        Space(2, 'Ocean Apartment', 'Luxury stay by the sea', 200, 2),
        Space(3,'Alehouse', 'free beer', 250, 1)
    ]

def test_delete_space(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    space_repository = SpaceRepository(db_connection)
    space_repository.delete(1)
    assert space_repository.all() == [Space(2, 'Ocean Apartment', 'Luxury stay by the sea', 200, 2)]


