import unittest  # Importing the unittest module
import pyperclip

from detail import Detail  # Importing the detail class


class TestDetail(unittest.TestCase):
    # import pyperclip
    '''
    Test class that defines test cases for the detail class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_detail = Detail(
            "xyz", "xyz", "2222222222", "xyz@user.com")  # create detail object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_detail.user_name, "xyz")
        self.assertEqual(self.new_detail.user_name, "xyz")
        self.assertEqual(self.new_detail.account_password, "2222222222")
        self.assertEqual(self.new_detail.email, "xyz@user.com")
    
