# importing modules and files
import banks
import customer_database
import customer
from customer_database import customers
import art
from time import sleep
import sys
import time
import random

# making sure the machine is on for the application to run
is_on = True

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

# creating a function that types out strings super fast instead of printing them
def type_super_fast(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    print('\n')

# creating a function to allow the user to continue or exit after something big happens in the application
def user_choice_application():
    print('\n')
    user_option = input("Do you want to continue?(yes/no): ")
    if user_option == 'yes':
        application()
    else:
        exit()

# creating a function to allow the user to try again or exit after making a mistake
def user_choice_initial():
    print('\n')
    user_option = input("Let's try again?(yes/no): ")
    if user_option == 'yes':
        initial_screen()
    else:
        exit()

# creating a login function so the customer can login with their details they put in earlier when they registered
def login_customer():
    user_username = input('Enter your username: ')
    if user_username != customer_database.customers.get('username'):
        type_fast('Sorry incorrect username. \nPlease try again')
        type_slow('Restarting...     ')
        initial_screen()
    else:
        user_password = input('Enter your password: ') 
    
    if user_password != customer_database.customers.get('password'):
        type_fast('Sorry incorrect password. \nPlease try again')
        type_slow('Restarting...     ')
        initial_screen()
    else:
        type_slow('Checking login...')
        sleep(2)
        type_super_fast('\033[5;32m Login accepted \033[0;0m')
        type_fast('Proceeding to main menu!')
        application()

# creating a function to contact customer support
def contact_support():
    ticket_number = random.randint(10000,30000)
    name = customers.get('name')
    surname = customers.get('surname')
    email = customers.get('email')
    phone = customers.get('phone')
    msg = input('How can customer support help you today?: ')

    type_fast("The following information is being sent to the bank:")
    type_super_fast("----------------------------------------------------")
    type_fast("Name: " + str(name))
    type_fast("Surname: " + str(surname))
    type_fast("Email: " + str(email))
    type_fast("Phone number: " + str(phone))
    type_fast("Message: " + str(msg))
    type_super_fast("----------------------------------------------------")
    type_fast("Please, wait while we process the information.......")
    sleep(2)
    type_fast("Message sent!")
    type_fast("Please, wait while we create a support ticket.......")
    sleep(4)
    type_fast("Support ticket created")
    type_super_fast("----------------------------------------------------")
    type_fast("Support ticket #" + str(ticket_number))
    type_fast("Name: " + customers.get('name'))
    type_fast("Surname: " + customers.get('surname'))
    type_fast("Email: " + customers.get('email'))
    type_fast("Phone number: " + customers.get('phone'))
    type_fast("Message: " + str(msg))
    type_super_fast("----------------------------------------------------")
    type_fast("Our staff is going to contact you as soon as we can. Thank you for contacting us!")
    application()

# creating a login menu before the main application runs with the main menu
def initial_screen():
    while is_on:
        print(art.art)
        type_super_fast('\033[5;33m ----------------------------------------------------------- \033[0;0m')
        type_fast("Please, choose the option you would like to proceed with")
        type_fast("1. Register")
        type_fast("2. Login")
        type_fast("3. Exit")
        type_super_fast('\033[5;36m ----------------------------------------------------------- \033[0;0m')
        customer_option_one = input("Enter your option here: ")

        if customer_option_one == '1':
            print('\n')
            customer_database.CustomerDatabase.register_name()
            customer_database.CustomerDatabase.register_surname()
            customer_database.CustomerDatabase.register_email()
            customer_database.CustomerDatabase.register_phone()
            customer_database.CustomerDatabase.register_username()
            customer_database.CustomerDatabase.register_password()
            customer_database.CustomerDatabase.confirm_password()
            customer_database.CustomerDatabase.registration_complete()
            type_fast("Taking you back to the login menu...")
            sleep(2)
            initial_screen()
        elif customer_option_one == '2':
            print('\n')
            login_customer()
        elif customer_option_one == '3':
            print('\n')
            type_fast("Thank you and hope to see you soon!")
            exit()
        elif customer_option_one == '101':
            type_fast("Dev mode entered")
            application()
        else:
            type_fast("Wrong input")
            user_choice_initial()

# creating the main menu
def application():
    print(art.art)
    type_super_fast('\033[5;33m ----------------------------------------------------------- \033[0;0m')
    type_fast("Please, choose the option you would like to proceed with")
    type_fast("1. Available banks and rates")
    type_fast("2. Calculate the mortgage")
    type_fast("3. Contact support")
    type_fast("4. Exit")
    type_super_fast('\033[5;36m ----------------------------------------------------------- \033[0;0m')
    customer_option_two = input("Enter your option here: ")

    if customer_option_two == '1':
        print('\n')
        banks.Banks.__repr__()
        user_choice_application()
    elif customer_option_two == '2':
        print('\n')
        customer.Customer.user_inputs()
        print('\n')
        type_fast('The loan you would receive is:')
        type_fast('£' + str(customer.Customer.loan_amount))
        type_fast('What you would have to repay with interest is:')
        type_fast('£' + str(customer.Customer.loan_with_interest))
        type_fast('You would have to pay this over {rt} months in increments of £{mp}.'.format(rt = customer.Customer.repayment_time_int, mp = customer.Customer.monthly_payment_rounded))
        user_choice_application()
    elif customer_option_two == '3':
        print('\n')
        contact_support()
    elif customer_option_two == '4':
        print('\n')
        type_fast("Thank you and hope to see you soon!")
        exit()
    else:
        type_fast("Wrong input")
        user_choice_application()

initial_screen()