from credential import Credential
from user import User
import random


def create_user(fullname,email,mobilenumber):
    """
    This function generates username
    """

    new_user = User(fullname,email,mobilenumber)
    return new_user

def create_credential(username, psword, email):
    """
    This function generates credentials for a new user
    """

    new_credential = Credential(username,psword,email)
    return new_credential    

def save_user(user):

    user.save_user_details()


def save_cred(credential):
    """
    This function Saves users'credentials
    """
    credential.save_credential()

def del_user(user):
    """
    This Function to delete a user
    """
    user.delete_user()

def del_cred(credential):
    """
    This Function to delete all users credentials
    """
    credential.delete_credential()

