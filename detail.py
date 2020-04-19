
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
   

    def delete_detail(self):
        '''
        delete_detail method deletes a saved detail from the detail_list
        '''

        Detail.detail_list.remove(self)
                                



  