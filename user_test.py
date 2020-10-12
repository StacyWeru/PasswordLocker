import unittest
from user import User


class TestUser (unittest.TestCase):

    '''
    Test class that defines test caes for the user class behaviours

    Args:
    unittest.TestCase : TestCase class that helps in creating test classes

    '''

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''

    self.new_user = User ("Ace","Cant3672S")

def test_init(self):

    '''
    test_init test case to test i the object is initialized properly

    '''

    self.assertEqual(self.new_user.user_name,"Ace")
    self.assertEqual(self.new_user.password,"Cant3672S")


    if __name__ == '__main__':
        unittest.main()