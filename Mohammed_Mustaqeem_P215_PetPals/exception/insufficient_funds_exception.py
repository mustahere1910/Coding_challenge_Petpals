class InsufficientFundsException(Exception):
    def __init__(self, message="Donation amount is insufficient. Minimum allowed is $10."):
        self.message = message
        super().__init__(self.message)
