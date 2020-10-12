import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp (self):

        '''
        SetUp method to run before each test case
        '''

        self.new_credentials = Credentials ("Stacy" ,"Weru" ,"0712345678","stacyweru@gmail.com")

    def test_init(self):

        '''
        To test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.first_name, "Stacy")
        self.assertEqual(self.new_credentials.last_name, "Weru")
        self.assertEqual(self.new_credentials.phone_number, "0712345678")
        self.assertEqual(self.new_credentials.email_address, "stacyweru@gmail.com")


    def test_save_credentials(self):

        '''
        To test if the credential objects were savd into the credentials list

        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):

        '''
        To clean up after each test run
        '''

        Credentials.credential_list = []

    def test_save_nultiple_credentials(self):

        '''
        To check if we can save multiple credentials to our list

        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Test","Credentials" ,"88635328316","credentials@roflmao.com") 

        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credentials(self):

        '''
        To check if we can remove credentials from our credentials list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Test","Credentials" ,"88635328316","credentials@roflmao.com") 

        test_credentials.save_credentials()

        self.new_credentials.delete_credentials ()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credentials_by_email(self):

        '''
        Test to check if we can find a contact by email

        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Test","Credentials" ,"88635328316","credentials@roflmao.com") 

        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_email("credentials@roflmao.com")

        self.assertEqual(found_credentials.email_address,test_credentials.email_address)



if __name__ == '__main__':
    unittest.main()

