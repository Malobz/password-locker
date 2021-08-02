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
        
    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
        
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
    
    @classmethod
    def find_by_account(cls, accName):
        """
        Method that takes in account and return credentials
        """
        for credentials in cls.credentials_list:
            if credentials.account == accName:
                return credentials
                
    @classmethod
    def credentials_exist(cls, accName):
        '''
        Method that checks if credentials exists from the credential list.
        
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == accName:
                    return True

        return False
    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_list