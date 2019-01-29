import unittest 
from user import User


class TestUser(TestCase):
    """
      Defines test cases for the user class behaviours.
      Args:
        TestCase: A class that helps create the test cases.
    """

    def setUp(self):
        """
          Method to run before the test cases.
        """
        self.new_user = User('Winston', 'Carlos', 'carlos_2_w', 'qwerty98')

    def test_init(self):
        """
          Test case to see if the object is being initialized properly.
        """
        self.assertEqual(self.new_user.first_name, 'winston')
        self.assertEqual(self.new_user.last_name, 'Carlos')
        self.assertEqual(self.new_user.username, 'carlos_2_w')
        self.assertEqual(self.new_user.password, 'qwerty98')

    def test_save_user(self):
        """
          Test case to see if objects are being stored on user_list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_user_exists(self):
        """
          Test case to see if a specified user exists.
        """
        self.new_user.save_user()
        self.assertTrue(User.user_exists('carlos_2_w'))


if __name__ == '__main__':
    main()