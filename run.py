from credential import Credential
from user import User
import random


def create_user(fullname,email,mobilenumber):
    """
    This function generates username
    """

    new_user = User(fullname,email,mobilenumber)
    return new_user
