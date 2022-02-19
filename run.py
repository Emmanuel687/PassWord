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

