class User:

    '''
    Create this class user to generate the user instance
    '''

    user_list = []

def __init__ (self,user_name,user_password):
    self.user_name = user_name
    self.user_password = user_password

def save_user(self):
        '''
        To create an instance of the user and save 
        '''
        User.user_list.append(self)

def delete_user(self):

    '''
    deletes a saved ueser from user_lidt
    '''

    User.user_list.remove(self)

@classmethod
def user_exists (cls,password):

    '''
    Method that checks if user exists in user_list

    Arg:
        
        password : Takes in password  to serach if it exists

        returns: 
        Boolean : True of flase depending if user exists

    '''

    for user in cls.user_list:
        if user_password == password :
            return True
        else:
            return False








