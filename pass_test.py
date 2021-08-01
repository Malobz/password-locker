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
        