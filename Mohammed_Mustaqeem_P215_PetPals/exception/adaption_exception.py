class AdoptionException(Exception):
    def __init__(self, message="An error occurred during the adoption process."):
        self.message = message
        super().__init__(self.message)
