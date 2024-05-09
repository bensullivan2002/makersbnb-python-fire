from lib.availability import *

class AvailabilityRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_availability(self, availability):
        self._connection.execute('INSERT INTO dates_available (start_date, end_date, space_id) VALUES (%s, %s, %s)',
                                 [availability.start_date, availability.end_date, availability.space_id])

    def find_by_space_id(self, space_id):
        rows = self._connection.execute('SELECT * FROM dates_available WHERE space_id = %s', [space_id])
        return [Availability(row['start_date'], row['end_date'], row['space_id']) for row in rows]
