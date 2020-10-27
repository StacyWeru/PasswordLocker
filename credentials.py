import pyperclip
import string
import random

class Credentials:

    '''
    A class created to generate the credentials instance

    '''

    #I am going to assume credentials are like phone number ,email number, etc

    credential_list = []
    status =""


    def __init__(self,first_name,last_name,phone_number,email_address):
        '''
        THis helps us to define properties of our objects

        '''

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address


    def save_credentials(self):

        '''
        To save credentials into the credentials list
        '''

        Credentials.credential_list.append(self)

    def delete_credentials(self):

        '''
        To delete a saved credential from the credential list
        '''

        Credentials.credential_list.remove(self)

    @classmethod

    def find_by_email(cls,email_address):

        '''
        Takes in the email address and returns the credentials that match
        '''

        for credentials in cls.credential_list:
            if credentials.email_address == email_address:
                return credentials

    def generate_password (self ,size =8 , char = string.ascii_uppercase+string.ascii_lowercase+string.digits):

        generate_password =''.join(random.choice(char) for _ in range(size))

        return generate_password


    @classmethod
    def credentials_exist (cls, user_name):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            user_name: user_name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credential_list:
            if credentials.user_name == user_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list



    
    
