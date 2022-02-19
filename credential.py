class Credential:
    pass
    credentials_array = []

    def __init__(self,userName,password,email):
        self.userName = userName
        self.password = password
        self.email = email
    """
    function for saving user credentials
    """
    def save_credentials(self):

        Credential.credentials_array.append(self)
    """
    function that displays user credentials
    """
    @classmethod
    def display_credentials(cls):

        return cls.credentials_array  
