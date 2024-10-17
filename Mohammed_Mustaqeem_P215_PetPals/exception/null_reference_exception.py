class NullReferenceException(Exception):
    def __init__(self, message="A pet's property is null."):
        self.message = message
        super().__init__(self.message)
