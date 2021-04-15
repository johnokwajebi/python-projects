# register
#- (first name and lastname or email) and password

#Login
# - account number and password


#Bank operations


#initialising the system
import random as random
import datetime 
database = {1234567890 : ['John', 'Okwajebi', 'jaykwa@gmail.com', 'passwordjohn', ]}


##def existing_database():
##    
##name = input('What is your username?\n')
##allowed_users = ['John', 'Mike', 'Grace']
##allowed_password = ['passwordjohn', 'passwordmike', 'passwordgrace']
##current_date= datetime.datetime.now()
##
##
##
##if (name in allowed_users):
##    password = input('Your Password?\n')
##    user_id =allowed_users.index(name)



def init():
    print('Welcome to Bank PHP')

    haveAccount = int(input('Do you have account with us:\n 1 (yes)\n 2 (no)\n'))

    if (haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('You have selected invalid option')
        init()

def login():
    print('******Login******')

    accountNumberFromUser = int(input('What is your account number?\n'))
    password = input('What is your password \n')
    for accountNumber,userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    bankOperation(userDetails)
                    
    print('Invalid account or password')
    Validate = int(input('(1) Try again (2) Register\n'))
    if Validate == 1:
        login()
    else:
        register()
   
    

def register():
    print('*******Register*******')

    email = input('What is your email address?\n')
    first_name = input('What is your first name\n')
    last_name = input('What is your last name\n')
    password = input('Create a password\n')

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name,last_name,email,password]
    

    print('Your account has been created')
    print("===== ===== ===== ===== ")
    print(f'Your account number is: {accountNumber}')
    print("===== ===== ===== =====")

    # something for giving a current balance of customer after they register
    login()

def bankOperation(user):
    print(f'Welcome {user[0]}, {user[1]}')
    

    selectedOption = int(input('What would you like to do? \n (1) Deposit (2) Withdrawal\n (3) Complaint (4) Logout\n (5) Exit \n'))
    if selectedOption == 1:
        depositOperations()
        doneOperations()
    elif selectedOption == 2:
        withdrawalOPerations()
        doneOperations()
    elif selectedOption == 3:
        complaintOperations()
        doneOperations()
    elif selectedOption == 4:
        login()
    elif selectedOption == 5:
        exit()
    else:
        print('Invalid option selected, Please select an option listed below')
        bankOperation(user)


def withdrawalOPerations():
    # get current balance
    #get amount to withdraw
    #check if current balance > withdraw amount
    # deduct withdraw amount from current balance
    #display current balance
    cash = input('How much would you like to withdraw?\n')
    print('Take your cash:', cash)
def depositOperations():
    deposit = input('How much would you like to deposit?\n')
    print('Your current balance is:', deposit)
def complaintOperations():
    complaint = input('What issue would you like to report?\n')
    print('Thank you for contacting us. Your "{}" complaint is received, Our customer service agent will get back to you within 24 hours'.format(complaint))
def doneOperations():
    print('Would you like to perform another transaction?')
def fetch_current_balance(userDetails):
    return userDetails[4]
def set_current_balance(userDetails, balance):
    userDetails[4] = balance

    trans = int(input(' Press (1) to perform another transaction\n (2) To exit '))
    if trans == 1:
        login()
    elif trans == 2:
        print('Please take your card')
        exit()
    else:
        print('Please select a valid option')
        doneOperations()

def logout():
    login()
def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)



#### Actual Banking System ####
init()
