from user import User
from credentials import Credentials

def create_user(first_name,last_name,user_name,email):
    '''
    Function t create new user
    '''

    new_user = User(first_name,last_name,user_name,email)
    return new_user


def create_credentials(first_name,last_name,phone_number,email_address):
    new_credentials = Credentials(first_name,last_name,phone_number,email_address)
    return new_credentials


def generate_password():
	'''
	Function to generate a password automatically
	'''
	generate_password = Credentials.generate_password()
	return generate_password

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credentials(credentials):

    credentials.save_credentials()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credentials(credentials):

    credentials.delete_credentials()


def find_user(user_name):
    '''
    Function that finds a user by user_name and returns the user
    '''
    return User.find_by_user_name(user_name)

def find_credentials(user_name):

    return Credentials.find_by_email(user_name)


def check_existing_user(user_name):
    '''
    Function that check if a user exists with that user_name and return a Boolean
    '''
    return User.user_exist(user_name)

def check_existing_credential(user_name):

    return Credentials.credentials_exist(user_name)


def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def display_credential():

    return Credentials.display_credentials()


def main():

    print("Hello!Welcome to Password Locker")
    # print("/n")
    print("Do you have an account or  would you like to register with us?")
    print("if you would like to join us please type in 'create'")
    print ("If you would like to see your credentials please type in 'display'")
    print ("If you would like us to generate your pasword please type in 'generate'")
    print ("If you would like us to delete your account plese type in 'delete'")
    select = input("")

    if select == "create ":
    # newUser()
        print("Welcome user Please type in you first name")
        first_name = input()

        print("Your last name ")
        last_name = input ()

        print("Username")
        username = input()

        print("Email Address")
        email_address = input()

        print("Password")
        password = input()

        save_user(create_user(first_name,last_name,username,email_address))
        print ('\n')
        print (f"New account {first_name}{last_name} created")
        print ('\n')

    elif select== "display":
        
        if display_credential():
            print("Here are your credentials")
            print('\n')


            for user in display_user():
                print(f"{user.first_name} {user.last_name} {user.username} ")

                print('\n')

        else :
                print("Sorry we cant find your credentials")
                print('\n')

    elif select == "generate":

        print("Your passwor will be auto-generated")

        print("Please input your first name ")
        first_name = input()

        print("Please input your first name ")
        last_name = input()

        print("Please input your first name ")
        phone_number = input()

        print ("Please input your email address")
        email_address = input()

        print('\n')
        print("Enter Password ")
        password = generate_password()

        save_credentials(create_credentials(first_name,last_name,phone_number,email_address))

        print('\n')

        print(f"New Credentials for {first_name} {last_name} created.Your password is {password} ")

        print('\n')

    elif select == "delete":

        print("Just so you know there is no going back")
        print("Please enter uour email  ")
        delete_email = input("")

        del_credentials(delete_email)


    else: 

        print("It is done ! Have a nice day")


    if __name__ == '__main__':
        main()









