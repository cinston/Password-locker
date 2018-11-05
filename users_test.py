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
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Carlos Stone")
        self.assertEqual(self.new_user.password,"Zapper")    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)    