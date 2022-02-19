import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Emmanuel Koech","koechemmanuel.gmail.com","0713598794")
    def tearDown(self):

        User.user_array = []

    def test_init(self):

        self.assertEqual(self.new_user.full_name,"Emmanuel Koech")
        self.assertEqual(self.new_user.email,"koechemmanuel2002@gmail.com")
        self.assertEqual(self.new_user.mobile_number,"0713598794")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user_details()
        self.assertEqual(len(User.user_array), 1)    

    def test_save_multiple_users(self):
        '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
       '''
        self.new_user.save_user_details()
        test_user = User("Test", "user", "user@gmail.com", "0713598794") 
        test_user.save_user_details()
        self.assertEqual(len(User.user_array), 2) 

    def test_display_all_users(self):

        self.assertEqual(User.display_users(), User.user_array) 


if __name__ == '__main__':
    unittest.main()             