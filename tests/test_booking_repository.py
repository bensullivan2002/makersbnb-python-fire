from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import datetime
"""
When I use find I get a user back by their user_id
"""
def test_get_booking_back_based_on_id(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    booking_repository = BookingRepository(db_connection)
    result = booking_repository.find(1)
    assert result == Booking(1, datetime.strptime('2024-05-12', '%Y-%m-%d').date(), datetime.strptime('2024-05-19', '%Y-%m-%d').date(), 1, 2)
    
    
    
    """
When I use findbookingbyuserid I get a list of bookings back from by their user_id
"""
def test_get_list_of_bookings_from_user_id(db_connection):
    db_connection.seed('seeds/makersbnb_fire.sql')
    booking_repository = BookingRepository(db_connection)
    result = booking_repository.find_bookings_by_user_id(2)
    assert result == [
        Booking(2, datetime.strptime('2024-07-13', '%Y-%m-%d').date(), datetime.strptime('2024-07-28', '%Y-%m-%d').date(), 2, 1),
        Booking(3, datetime.strptime('2024-06-15', '%Y-%m-%d').date(), datetime.strptime('2024-06-30', '%Y-%m-%d').date(), 2, 1)
        ]

