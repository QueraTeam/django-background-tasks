class BackgroundTaskError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class InvalidTaskError(BackgroundTaskError):
    """
    The task will not be rescheduled if it fails with this error
    """
