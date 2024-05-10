from lib.booking import Booking
import datetime

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES (%s, %s, %s, %s)', [booking.start_date, booking.end_date, booking.user_id, booking.space_id])
        return None 
    
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            booking =  Booking(row["id"], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
            bookings.append(booking)
        return bookings
    
    def find(self, booking_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id=%s', [booking_id])
        row = rows[0]
        booking = Booking(row["id"], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
        return booking
    
    def find_bookings_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE user_id=%s', [user_id])
        bookings = []
        for row in rows:
            booking = Booking(row["id"], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
            bookings.append(booking)
        return bookings
