import unittest
from pass_locker import User
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
        
        
if __name__ == '__main__':
    unittest.main()
        
        