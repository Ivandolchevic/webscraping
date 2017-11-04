""" All custom exceptions """

class NavigationFailed(Exception):
    """ Error raised on when the connection failed  """
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return repr(self.message)