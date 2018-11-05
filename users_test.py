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
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("cinston warlos", "waga") # new user
        test_user.save_user()
        #print(test_user.username)
        self.assertEqual(len(User.user_list),2)
    def test_auth_user(self):
        '''
        test to check if we can find a user by username/password and display information
        '''

        self.new_user.save_user()
        test_user = User("cinston warlos", "waga") # new user
        test_user.save_user()

        found_user = User.find_by_userpass("cinston warlos", "waga")

        self.assertEqual(found_user.username,test_user.username)
 



 if __name__ == '__main__':
    unittest.main()                