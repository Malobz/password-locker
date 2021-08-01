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
        
    def save_user(self):
        """
        saves user objects into user_list
        """
        User.user_list.append(self)
        
    def delete_user(self):
        """
        delete saved user from user list
        """
        User.user_list.remove(self)
        
class Credentials:
    """
    Generates new instances of class Credentials
    """
    credentials_list = []
    
    def __init__(self, account, username, password):
        
        """
    Defining properties for our objects
    Args:
    account
    username 
    Password
        """
        self.account = account
        self.username = username
        self.password = password
        
    def save_credentials(self):
        """
        saves user objects into credentials_list
        """
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        """
        delete saved credentials from credentials list
        """
        Credentials.credentials_list.remove(self)
   
    