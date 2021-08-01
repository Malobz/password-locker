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
        
if __name__ == '__main__':
    unittest.main()
        
        