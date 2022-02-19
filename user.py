class User:
    """
    creates new user instances
    """
    pass

    user_array = []

    def __init__(self,fullName,email,mobileNumber):
        self.fullName = fullName
        self.email = email
        self.mobileNumber = mobileNumber

    def saveUserDetails(self):

        User.user_array.append(self)

    @classmethod
    def display_users(cls):

        return cls.user_array


        pass





        