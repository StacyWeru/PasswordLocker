from user import User

print("Hello!Welcome to Password Locker")
# print("/n")
print("Do you have an account or  would you like to register with us?")
print("If you do please type in 'login' ,if you would like to join us please type in 'create'")
select = input("")

if select == "create ":
    newUser()
    print("Are you sure you want to try this?")
elif select == "login ":
    oldUser()
    print("Welcome back!")

    def newUser():
        user_name = input("Please create your username")

        if user_name in user:
            print("That username is already being used .Please choose another")
        else:
             password = input ("Please create your password")
             user[user_name] = password
             print("Account successful")

    def oldUser():
        login = input("Please login with username")
        pass_word = input ("Please enter password")

        if login in user and user[user_name] == pass_word:
                 print ("Login successful")
        else:
                print ("Sorry the account doesn't exit  or maybe wrong password")
            

