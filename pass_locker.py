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
        
    
   
    