from credential import Credential
from user import User
import random


def create_user(fullname,email,mobilenumber):
    """
    This function generates username
    """

    new_user = User(fullname,email,mobilenumber)
    return new_user

def create_credential(username, password, email):
    """
    This function generates credentials for a new user
    """

    new_credential = Credential(username,password,email)
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

def display_user():
    """
    This Function that returns saved users
    """
    return User.display_users()

def display_cred():
    """
    This function that returns saved user credentials
    """
    return Credential.display_credential()
# As a user, I want to create a password locker account with my details, a login username and password.
# As a user, I want to store my already existing account credentials in the application. Assuming I already have a twitter account, I want to store my already existing twitter username and password in the application.
# As a user, I want to create new account credentials in the application. For example, if I have not yet signed up for Instagram, I would want to create a credentials account for Instagram in the application and the application generates a password for me to use when I sign up for Instagram.
# As a user, I want to have the option of putting in a password that I want to use for the new credential account. For example, when creating my Instagram credential account, I want to have an option of putting in the password I want to use instead of having the application generate a password for me.
# As a user, I also want to view my various account credentials and their passwords in the application.
# As a user, I want to delete a credentials account that I no longer need in the application.
def main():

    print("Hello,To proceed choose an option and type the command of any below.Thank you")

    while True:
        print("\n sh - (Sign up Option) for a new user account\n ac- (Create Account Option) a new account with autogenerated password\n da - (Display all user Option) accounts \n ex -(exit option) the contact list \n")            

        short_code = input().lower()

        if short_code == 'sh':
            print("New user")
            print("-"*10)
            print("Hello,Which Account would you like to create?")
            account = input()
            print(f"We will let you into your {account} in a few")

            print("Input Your Full name")
            full_name = input()

            print("Input Your E-mail")
            email = input()

            print("Input your Mobile Number")
            mobile_number = input()

            print("Input Username")
            user_name = input()

            print("Input Password")
            psword = input()

            save_user(create_user(full_name,email,mobile_number))   
            
            print('\n')
            print(f"A new{account} has been created by {full_name}")
            print(f" The username is {user_name} and password {psword} ")
            print('\n')

        elif short_code == 'ac':
            print("New user")
            print("-" * 10)
            print("What type of Account would you like to create?")
            account = input()
            print(f"You will have your {account} account created soon")

            print("Name")
            full_name = input()

            print("Email...")
            email = input()

            print("Phone number..")
            mobile_number = input()

            print("Username..")
            user_name = input()

            p = "0000"
            psword = "".join(random.sample(p, 8))

            save_user(create_user(full_name,email,mobile_number))
            save_cred(create_credential(user_name,psword,email))
            print('\n')
            print(f"A new {account} will be created by {full_name}")
            print(f"Username{user_name} password {psword} ")
            print('\n')

        elif short_code == 'da':

            if display_user():
                print("Here are your accounts")
                print('\n')

                for user in display_user():
                    print(f"{user.full_name} has an account for {account}")

                print('\n')
            else:
                print('\n')
                print("You do not have an existing account")
                print('\n')

        elif short_code == 'ex':
            print("ThankYou and See You")
            break
        else:
            print(":(No command allowed")


if __name__ == '__main__':
    main()
