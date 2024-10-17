from util.db_conn_util import db_connection  # Import the established database connection

class DonationDAO:
    def __init__(self):
        self.connection = db_connection  # Use the imported connection directly

    def record_cash_donation(self, donor_name: str, amount: float):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Donations (donor_name, amount) VALUES (?, ?)", (donor_name, amount))
        self.connection.commit()

