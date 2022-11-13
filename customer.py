# importing modules and files
import banks
import time
import sys
from time import sleep
import re

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

# create a class for the customer
class Customer():
    user_dict = {}
    loan_amount = 0
    interest_rate = 0
    loan_with_interest = 0
    repayment_time_int = 0
    monthly_payment = 0
    monthly_payment_rounded = 0

# making a function to return user inputs
    def user_inputs():
        down_payment = input('How much would you like to give as a down payment? \nPlease enter here: ')
        regex = re.match(r"^[0-9]{1,20}$", down_payment)
        if regex:
            print('')
        else:
            type_fast('Invalid input, must be a number. Please try again')
            exit()
        purchase_price = input('What is the value of the property you are trying to purchase? \nPlease enter here: ')
        regex = re.match(r"^[0-9]{1,20}$", purchase_price)
        if regex:
            print('')
        else:
            type_fast('Invalid input, must be a number. Please try again')
            exit()
        repayment_time = input('How long do you need to repay the loan with interest? (in months) \nPlease enter here: ')
        regex = re.match(r"^[0-9]{1,20}$", repayment_time)
        if regex:
            print('')
        else:
            type_fast('Invalid input, must be a number. Please try again')
            exit()
        bank_selection_input = input('What bank would you like to apply for a mortgage with? \nPlease enter here: ')
        if bank_selection_input in banks.Banks.available_banks.keys():
            type_slow('Calculating...')
            sleep(3)
        else:
            print('Sorry we do not provide this service for that bank. Please try again.')
            exit()

# adding user inputs into the dictionnary user_dict in a key:value form
        Customer.user_dict['down_payment'] = down_payment
        Customer.user_dict['purchase_price'] = purchase_price
        Customer.user_dict['repayment_time'] = repayment_time
        Customer.user_dict['bank_selection'] = bank_selection_input

# calculating everything needed for the application goal
        Customer.repayment_time_int = int(repayment_time)
        Customer.loan_amount = int(purchase_price) - int(down_payment)
        Customer.interest_rate = Customer.repayment_time_int * banks.Banks.available_banks.get(bank_selection_input)
        Customer.loan_with_interest = Customer.interest_rate * Customer.loan_amount + Customer.loan_amount
        Customer.monthly_payment = Customer.loan_with_interest / Customer.repayment_time_int
        Customer.monthly_payment_rounded = round(Customer.monthly_payment, 2)