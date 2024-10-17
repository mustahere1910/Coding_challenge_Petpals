from util.db_conn_util import db_connection  # Import the established database connection

class AdoptionEventDAO:
    def __init__(self):
        self.connection = db_connection  # Use the imported connection directly

    def fetch_upcoming_events(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM AdoptionEvents")
        return cursor.fetchall()
