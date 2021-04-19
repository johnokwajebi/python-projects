# register
#- (first name and lastname or email) and password

#Login
# - account number and password

#Bank operations

#initialising the system
import random as random
import datetime 

current_date= datetime.datetime.today()
database = {1234567890 : ['John', 'Okwajebi', 'jaykwa@gmail.com', 'passwordjohn', 0.0]}
##def existing_database():
##    

def init():
    print('Welcome to Bank PHP')

    have_account = int(input('Do you have account with us:\n 1 (yes)\n 2 (no)\n'))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('You have selected invalid option')
        init()

def login():
    print('******Login******')

    account_number_from_user = (input('What is your account number?\n'))
    is_valid_account_number = account_number_validation(account_number_from_user)
    
    if is_valid_account_number:
        password = input('What is your password \n')
        for account_number,user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bank_operations(user_details)
                        
    print('Invalid account or password')
    validate = int(input('(1) Try again (2) Register\n'))
    if validate == 1:
        login()
    elif validate == 2:
        register()
    else:
        print('Invalid option selected')
        init()
   

def register():
    print('*******Register*******')

    email = input('What is your email address?\n')
    first_name = input('What is your first name\n')
    last_name = input('What is your last name\n')
    password = input('Create a password\n')
    current_balance = 0.0
    try:
        account_number = generate_account_number()
    except ValueError:
        print('account generation failed')
        init()

    database[account_number] = [first_name,last_name,email,password,0]

    print(f'Your account has been created on {current_date}')
    print("===== ===== ===== ===== ")
    print(f'Your account number is: {account_number}')
    print("===== ===== ===== =====")
    print(f"Your current balance is: {current_balance}")
    # something for giving a current balance of customer after they register
    login()

def account_number_validation(account_number):
    ## check if acc number isnst empty
    ### if acc number is 10 digits
    ## if acc number is an integer
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("invalid input. Your account number should be digits")
                return False
            except TypeError:
                print("invalid account type")
                return False

            
            
        else:
            print('Account number cannot be less than 10 digits')
            return False

    else:
        print('Account number is a required field')
    

def bank_operations(user):
    print(f'Welcome {user[0]} {user[1]}. You logged in at {current_date}')
    

    try:
        selected_option = int(input('What would you like to do? \n (1) Deposit (2) Withdrawal (3) Current balance \n(4) Complaint (5) Logout (6) Exit \n'))

    
        if selected_option == 1:
            deposit_operations(user)
            done_operations()
        elif selected_option == 2:
            withdrawal_operations(user)
            done_operations()
        elif selected_option == 3:
            fetch_current_balance(user)
            done_operations()
        elif selected_option == 4:
            complaint_operations()
            done_operations()
        elif selected_option == 5:
            done_operations()
            login()
        elif selected_option == 6:
            exit()
        else:
            print('Invalid option selected, Please select an option listed below')
            bank_operations(user)
        
    except ValueError:
        print('Invalid option inputed. Please input a digit')
        bank_operations(user)
        

def deposit_operations(user):
    # get current balance
    #get amount to deposit and add to current balance
    # #display current balance
    try:
        
        input_deposit = float(input('Please enter the amount you want to deposit:\n'))
        user[4] = input_deposit + user[4]
        # current_balance = fetch_current_balance(user) + input_deposit
        print(f'You just deposited {input_deposit} in your account. Your new balance is {user[4]}')

    except ValueError:
        print('Invalid input. Please input a number')
        deposit_operations(user)   
    # print(f'You just deposited {input_deposit} in your account. Your new balance is {user_details[4]}\n')

def withdrawal_operations(user):
    # get current balance
    #get amount to withdraw
    #check if current balance > withdraw amount
    # deduct withdraw amount from current balance
    #display current balance
    try:
            
        cash = float(input('Please enter the amount you want to withdraw:\n'))
        if cash > user[4]:
            print(f'Insufficient funds, Please try again with a lower amount')
        else:
            user[4] = user[4] - cash
            print(f'Please take your cash of {cash}. Your new balance is {user[4]}')
    except ValueError:
        print('Invalid input. Please input a number')
        withdrawal_operations(user)
def complaint_operations():
    complaint = input('What issue would you like to report?\n')
    print(f'Thank you for contacting us. Your "{complaint}" complaint is received, Our customer service agent will get back to you within 24 hours')

def fetch_current_balance(user_details):
    print ('Your current balance is:',user_details[4])

def done_operations():
    print('Would you like to perform another transaction?')
    trans = int(input(' Press (1) to perform another transaction\n (2) To exit '))
    if trans == 1:
        init()
    elif trans == 2:
        print('Please take your card')
        exit()
    else:
        print('Please select a valid option')
        done_operations()


def logout():
    init()
def generate_account_number():
    return random.randrange(1111111111, 9999999999)



#### Running the ATM ####
init()
