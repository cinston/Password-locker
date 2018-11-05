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
        self.new_cred = Credential("Carlos Stone","Facebook", "Winston", "qwerti98")