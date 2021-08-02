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
    
