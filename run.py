#!/usr/bin/env python3.8
from pass_locker import User
from pass_locker import Credentials 

def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def create_credentials(acc, userName, passWord):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(acc, userName, passWord)
    return new_credentials

def save_credentials(credentia):
    '''
    Function to save contact
    '''
    credentia.save_contact()
    
def del_credentials(credentia):
    '''
    Function to delete credentials
    '''
    credentia.delete_credentials()
    
def find_credentials(account):
    '''
    Function that finds credentials by account name
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if credentials exists with that account and return a Boolean
    '''
    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def main():
    print("Hello Welcome to password locker. What would you like to do?")
    

    # rint(f"Hello {user_name}. what would you like to do?")
    # print('\n')

    while True:
            print("Use these short codes : ca - Create Account, lg- Log In ")

            short_code = input().lower()

            if short_code == 'ca':
                    print("Enter new credentials")
                    print("-"*20)

                    print("Username ...")
                    username = input()

                    print("Password ...")
                    password = input()

    
                    save_user(create_user(username, password)) # create and save new user.
                    print ('\n')
                    print(f"New user {username}  {password} created successfully")
                    print ('\n')

            elif short_code == 'lg':
                    
                    print("Enter your User name and Password to log in:")
                    print("-"*20)
                    username = input("Username: ")
                    password = input("Password: ")
                    print(f"Hello {username}.Welcome To PassWord Locker")  
                    print('\n')
                    
            while True:
                print("Use these short codes: cc - Create new credential  dc - View Credentials  fc - Find credential  d - Delete credential x - Exit the application ")
                short_code = input().lower()
                if short_code == "cc":
                    print("Create New Credential")
                    print("-"*20)
                    print("Account name ....")
                    acc = input().lower()
                    print("Your Account username")
                    userName = input()
                    print("Your Account password")
                    passWord = input()
                
                elif short_code == "dc":
                        if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credentials in display_credentials():
                                    print(f"{credentials.account} {credentials.username} .....{credentials.password}")

                            print('\n')
                else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')
                

                if short_code == "fc":

                    print("Enter the account you want to search for")

                search_account = input()
                if check_existing_credentials(search_account):
                        search_credentials = find_credentials(search_account)
                        print(f"{search_credentials.account} {search_credentials.username}")
                        print('-' * 20)

                        
                else:
                        print("That credential does not exist")
    
                if short_code == "d":
                    print("Enter the account name of the Credentials you want to delete")
                    search_account = input().lower()
                if find_credentials(search_account):
                    search_credential = find_credentials(search_account)
                    print("-"*20)
                    search_credential.delete_credentials()
                    print('\n')
                    print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                    print('\n')
                else:
                    print("That Credential you want to delete does not exist in your store yet")

                if short_code == "x":
                    print("bye. Thank you .......")
                    break
                else:
                    print("Enter valid input")
                            
if __name__ == '__main__':
    main()         
