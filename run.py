from detail import Detail

import pyperclip
import random
import string
import sys


def create_detail(u_name, lname, account, email):
    """
    Function to create a new detail

    """
    new_detail = Detail(u_name, lname, account, email)
    return new_detail

###We create a function called create_detail(), that takes in four arguments###

#####Save details #####


def save_details(detail):
    """
    Function to save detail
    """
    detail.save_detail()

### we create save detail function that takes in a detail object and then calls the save_detail method to save the detail. ####

#####Delete Detail


def del_detail(detail):
    """
    Function to delete a detail

    """
    detail.delete_detail()

### We create a del_detail function that takes in a detail object and then calls the delete_detail() method on the detail object deleting it from the detail list####

##Fininding a detail ##


def find_detail(password):
    """
    Function that finds a detail by password and returns the detail
    """
    return Detail.find_by_password(password)

### We create a func that takes in a password and calls the Detail class method find_by_password that returns the detail. ###

### Check if a detail exists ###


def check_existing_details(password):
    """
    Function that check if a detail exists with that password and return a Boolean
    """
    return Detail.detail_exist(password)

### The function check_existing_details takes in a password as an argument and calls the class method detail_exist which returns a boolean.###

## Displaying all details ##
def passsword(length):
    """Generate a random password."""
    alphabet = string.ascii_letters + string.digits
    while True:
        pw = ''.join(random.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in pw)
                and any(c.isupper() for c in pw)
                and any(c.isdigit() for c in pw)):
            break
    return(pw)

def display_details():
    """
    Func that rteturns all the saved details

    """
    return Detail.display_details()
### Deleting details ####
@classmethod
def delete_details():
    """
    Func that rteturns all the saved details

    """
    return Detail.delete_details()


## Copy Email ##
#**********************#


@classmethod
def copy_email(cls, password):
    """
    A funct that copies the email using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    detail_found = Detail.find_by_password(password)
    pyperclip.copy(detail_found.email)


