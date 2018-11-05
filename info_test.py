import unittest     #import unittest module
from info import Info   #import the user class


class TestInfo(unittest.TestCase):
    """
    Test class that defines test cases for the Info class behavioursself.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_info = Info("Carlos Stone","Facebook", "Winston", "qwerti98")
def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Info.info_list = []

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_info.username,"Carlos Stone")
        self.assertEqual(self.new_info.info_app,"Facebook")
        self.assertEqual(self.new_info.info_user,"Winston")
        self.assertEqual(self.new_info.info_pass,"qwerti98") 
 def test_save_info(self):
        '''
        test_save_contact test case to test if the passlock object is saved into
         the passlock list
        '''
        self.new_info.save_info() # saving the new info
        self.assertEqual(len(Info.info_list),1)
