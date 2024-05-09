from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
            rows = self._connection.execute("SELECT * FROM spaces")
            spaces = []
            for row in rows:
                space = Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"])
                spaces.append(space)
            return spaces

    def find(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"])
    
    def create(self, space):
        rows = self._connection.execute('INSERT INTO spaces (name, description, price_per_night, user_id) VALUES (%s, %s, %s, %s) RETURNING id', [
                                 space.name, space.description, space.price_per_night, space.user_id])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def delete(self, space_id):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [space_id])
        return None
    
    def update(self, space):
        self._connection.execute('UPDATE spaces SET name = %s, description = %s, price_per_night = %s, user_id = %s WHERE id = %s', [
                                 space.name, space.description, space.price_per_night, space.user_id])
        return space