class FileHandlingException(Exception):
    def __init__(self, message="File handling error occurred."):
        self.message = message
        super().__init__(self.message)
