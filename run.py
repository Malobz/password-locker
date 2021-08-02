#!/usr/bin/env python3.8
from pass_locker import User
from pass_locker import Credentials 

def create_user(userName, passWord):
    '''
    Function to create a new user
    '''
    new_user = User(userName, passWord)
    return new_user

def save_user(userr):
    '''
    Function to save user
    '''
    userr.save_user()
    
def del_user(userr):
    '''
    Function to delete a user
    '''
    userr.delete_user()
    
