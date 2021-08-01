class User:
    """
    Generates new instances of class User
    """
    user_list = []
    def __init__(self, username, password):
        
        """
    Defining properties for our objects
    Args:
    username :
    Password
        """
        self.username = username
        self.password = password