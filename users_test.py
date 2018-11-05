import unittest     #import unittest module
from users import Users   #import the user class


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behavioursself.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Carlos Stone","Zapper",)
    def tearDown(self):
            '''
        tearDown method that does clean up after each test case has run.
            '''
        User.user_list = []       