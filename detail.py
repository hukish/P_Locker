
import pyperclip
import random
import string
import sys

import random
import string
import sys


class Detail:

        """
    Class that generates new cases of details.
    """

    detail_list = []  # Empty detail list

    def __init__(self, user_name, account_name,password,email):

      # docstring removed for simplicity

        self.user_name = user_name
        self.account_name = account_name
        self.account_password = password
        self.email = email

    def save_detail(self):

        '''
        save_detail method saves detail objects into detail_list
        '''

        Detail.detail_list.append(self)
   

    def test_find_detail_by_password(self):
        '''
        test to check if we can find a detail by account password and display information
        '''

        self.new_detail.save_detail()
        test_detail = Detail("Test", "user", "2222222222",
                               "xyz@user.com")  # new detail
        test_detail.save_detail()

        found_detail = Detail.find_by_password("2222222222")

        self.assertEqual(found_detail.email, test_detail.email)