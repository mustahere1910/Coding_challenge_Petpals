from entity.donation import Donation
from datetime import datetime

class CashDonation(Donation):
    def __init__(self, donor_name, amount, donation_date):
        super().__init__(donor_name, amount)
        self.donation_date = donation_date

    def record_donation(self):
        # Logic to record cash donation
        pass
