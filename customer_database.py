# importing modules and files
from time import sleep
import time
import sys
import re

import customer

# creating an empty dictionary to store customer details they input
customers = {}


# creating a function that types out strings slow instead of printing them
def type_slow(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n')


# creating a function that types out strings fast instead of printing them
def type_fast(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    print('\n')


# creating a class for things related to customer input details
class CustomerDatabase:

    register_name = ''
    register_surname = ''
    register_email = ''
    register_phone = ''
    register_username = ''
    register_password = ''

    def register_name():
        user_first_name = input("Please enter your name below \nFirst name: ")
        regex = re.search(r"^[a-zA-Z]+$", user_first_name)
        if not regex:
            type_fast('First name should only contain letters. Please try again')
            sleep(2)
            CustomerDatabase.register_name()
        CustomerDatabase.register_name = user_first_name
        print(CustomerDatabase.register_name)

    def register_surname():
        user_surname = input("Surname: ")
        print('\n')
        regex = re.match(r"^[a-zA-Z]+$", user_surname)
        if not regex:
            type_fast('Surname should only contain letters. Please try again')
            sleep(2)
            CustomerDatabase.register_surname()
        CustomerDatabase.register_surname = user_surname
        print(CustomerDatabase.register_surname)

    def register_email():
        user_email = input('Please enter your email below \nEmail: ')
        regex = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_email)
        type_slow('Checking email...')
        sleep(2)
        if regex:
            type_fast('\033[5;32m Email valid \033[0;0m')
        else:
            type_fast('Invalid email address. Please try again')
            sleep(2)
            CustomerDatabase.register_email()
        CustomerDatabase.register_email = user_email
        print(CustomerDatabase.register_email)

    def register_phone():
        user_number = input('Enter your phone number below \nNumber: ')
        regex = re.match(r"^[0-9]{7,12}$", user_number)
        type_slow('Checking phone number...')
        sleep(2)
        if regex:
            type_fast('\033[5;32m Number valid \033[0;0m')
        else:
            type_fast('Invalid number. You should enter a number between 7 and 12 numbers long. Please try again')
            CustomerDatabase.register_phone()
        CustomerDatabase.register_phone = user_number
        print(CustomerDatabase.register_phone)

    def register_username():
        username = input("Please enter your username and password below \nUsername: ")
        regex = re.search(r"^[a-zA-Z0-9\_]+$", username)
        if not regex:
            type_fast('Username can only contain underscores, numbers and letters. \nPlease try again')
            CustomerDatabase.register_username()
        CustomerDatabase.register_username = username
        print(CustomerDatabase.register_username)

    def register_password():
        password = input("Password: ")
        regex = re.search(r"^[a-zA-Z0-9\_]+$", password)
        if not regex:
            type_fast('Passwords can only contain underscores, numbers and letters. \nPlease try again')
            CustomerDatabase.register_password()
        CustomerDatabase.register_password = password

    def confirm_password():
        confirm_password = input('Confirm password: ')
        type_slow('Checking password...')
        sleep(3)
        if confirm_password == CustomerDatabase.register_password:
            type_fast('\033[5;32m Password match! \033[0;0m')
        else:
            type_fast('Your password does not match. \nPlease try again.')
            CustomerDatabase.register_password()
        print(CustomerDatabase.register_password)


    def registration_complete():
        type_slow('We are registering you...')
        type_slow('Please wait!')
        sleep(2)
        customers['name'] = CustomerDatabase.register_name
        customers['surname'] = CustomerDatabase.register_surname
        customers['email'] = CustomerDatabase.register_email
        customers['phone'] = CustomerDatabase.register_phone
        customers['username'] = CustomerDatabase.register_username
        customers['password'] = CustomerDatabase.register_password
        print(customers)
        type_slow('Please wait!')
        sleep(4)
        type_fast("Customer created. You may now login with your username and password")