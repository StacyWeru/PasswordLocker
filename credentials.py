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
