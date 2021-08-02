import unittest
from pass_locker import User
from pass_locker import Credentials
class TestUser (unittest.TestCase):
    """
    Test class that defines test cases for the User class behaviours.
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Malobz", "kjdi") #create user object
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Malobz")
        self.assertEqual(self.new_user.password, "kjdi")
        
    def test_save_user(self):
        """
        test if user object is updated in user list
        """
        self.new_user.save_user() #save the new user
        self.assertEqual(len(User.user_list),1)
    
    
    def tearDown(self):
        """
        clean up after each test case has run.
        """
        User.user_list = []
    def test_save_multiple_user(self):
        """
        test to check if we can save multiple user
        """
        self.new_user.save_user()
        test_user = User("Mercy", "qwerty") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
        
    def test_delete_user(self):
        """
        test to see if you can remove user from the user_list
        """
        self.new_user.save_user()
        test_user = User("Mercy","quo")
        test_user.save_user()
        self.new_user.delete_user() #deleting user
        self.assertEqual(len(User.user_list),1)
        
    
class TestCredentials (unittest.TestCase):
    """
    Test class that defines test cases for the Credentials class behaviours.
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("Instagram", "Maloba", "scabz123") #create credentials object
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.account, "Instagram")
        self.assertEqual(self.new_credentials.username, "Maloba")
        self.assertEqual(self.new_credentials.password, "scabz123")
        
    def test_save_user(self):
        """
        test if user object is updated in user list
        """
        self.new_credentials.save_credentials() #save the new user
        self.assertEqual(len(Credentials.credentials_list),1)
    
    
    def tearDown(self):
        """
        clean up after each test case has run.
        """
        Credentials.credentials_list = []
    def test_save_multiple_credentials(self):
        """
        test to check if we can save multiple credentials
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "Moreen", "qwert") #new user
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    
        
    def test_delete_credentials(self):
        """
        test to see if you can remove credentials from the credentials_list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","Eugene","qaz")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials() #deleting user
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentials_by_accName(self):
        '''
        test to check if we can find credentials by account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Snapchat","Eugene","qaz") # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_accName("Snapchat")

        self.assertEqual(found_credentials.password,test_credentials.password)
    
                
        
if __name__ == '__main__':
    unittest.main()
        
        