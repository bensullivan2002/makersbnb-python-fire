from lib.booking import Booking

def test_formats_nicely():
    test_booking = Booking(1, '2024-05-12', '2024-05-19', 1, 2)
    assert str(test_booking) == "Booking(1, 2024-05-12, 2024-05-19, 1, 2)"

def test_booking_are_equal():
    test_booking1 = Booking(1, '2024-05-12', '2024-05-19', 1, 2)
    test_booking2 = Booking(1, '2024-05-12', '2024-05-19', 1, 2)
    assert test_booking1 == test_booking2