class Category:
  name = ""
  #To instantiate between objects
  def __init__(self, name,if_false = False):
    self.name = name
    self.balance = 0.0
    self.ledger = list()
    self.if_false = if_false

   #Check funds method
  def check_funds(self, amount):
    if float(amount) > self.balance:
      if_false = "insufficient funds: Your current balance is {}".format(Category.get_balance(self))
      return if_false
    else:
      return ("You can access {} from your current balance of {}".format(amount,(Category.get_balance(self))))

  #Deposit method
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : amount, "description" : description})
    self.balance = self.balance + float(amount)

  #Withdraw method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount) == self.if_false :
      return "Insufficent Funds for {}".format(description)
    else:
      self.ledger.append({"amount" : (0 - amount), "description" : description})
      self.balance = self.balance - float(amount)
      return "Take your cash: {} {}".format(amount,description )

  #Get balance method
  def get_balance(self):
    return self.balance

  #Transfer method
  def transfer(self, amount, category):
    if self.check_funds(amount) == False:
      return "Not sufficient for a transfer to {}".format(category.name) ### change made
    else:
      self.withdraw(amount, ("Transfer to " + category.name))
      category.deposit(amount, ("Transfer from " + self.name))
      return "Transfer has been made to {}".format(category.name)
  

def budget_operations():
    print ("Welcome to your budget app. What would you like to do??")
    budget_ops = int(input('Please input:\n1. Food 2. Entertainment \n3. Clothing 4. Start again 5. Exit app\n '))
    if budget_ops == 1:
        print('\n**************FOOD**************\n')
        food_operations()
    elif budget_ops == 2:
        print('\n**************ENTERTAINMENT*************\n')
        ent_operations()
    elif budget_ops == 3:
        print('\n**************CLOTHING (DRIPS)***************\n')
        clothing_operations()
    elif budget_ops == 4:
        budget_operations()
    elif budget_ops == 5:
        exit()
    else:
        print("Invalid input, please select from the available options")
        budget_operations()

food = Category('Food')
ent = Category('Entertainment') ## Ent stands for entertainment ##
clothing = Category('Clothing')

def food_operations():

    print ("Welcome to your Food. What would you like to do??\n")
    food_ops = int(input('Please input:\n 1. Deposit 2. Withdrawal 3. Transfer 4. Balance 5. Check funds 6. Home\n'))
    if food_ops == 1:
        input_deposit = int(input('Enter your Food budget:\n'))
        food.deposit(input_deposit)
        print(f'You just deposited {input_deposit} in your food wallet. Your new balance is {food.get_balance()}\n')
        food_operations()
    elif food_ops == 2:
        input_withdrawal = float(input('How much would you like to withdraw:\n'))
        input_desc = input("What are you withdrawing for:\n")
        if input_withdrawal > food.get_balance():
            print (f'insufficient funds for {input_desc}')
        elif input_withdrawal <= food.get_balance():
            print(food.withdraw(input_withdrawal, input_desc),'\n',f'Your balance after {input_desc} is:', food.get_balance(),'\n')
        food_operations()
    elif food_ops == 3:
        input_transfer = float(input('How much would you like to transfer:\n'))
        input_category = int(input("Which category do you want to transfer to: 1. Entertainment 2. Clothing\n"))
        if input_category == 1:
            if input_transfer > food.get_balance():
                print("Insufficient funds for transfer ")
            elif input_transfer <= food.get_balance():
                food.transfer(input_transfer,ent)
                print(f"Transfer of {input_transfer} was made from Food to Entertainment")
            else:
                print("Invalid input, please select from the available options")
                food_operations()
            food_operations()
        elif input_category == 2:
            if input_transfer > food.get_balance():
                print("Insufficient funds for transfer ")
            elif input_transfer >= food.get_balance():
                food.transfer(input_transfer,clothing)
                print(f"Transfer of {input_transfer} was made from Food to Clothing")
            else:
                print("Invalid input, please select from the available options")
                food_operations()
            food_operations()
    elif food_ops == 4:
        print(" Your food balance is:",food.get_balance())
        food_operations()
    elif food_ops == 5:
        input_check_funds = float(input('How much would you like to check:\n'))
        print(food.check_funds(input_check_funds))
        food_operations()
    elif food_ops == 6:
        budget_operations()
    else:
        print("Invalid input, please select from the available options")
        food_operations()

  
def ent_operations():

    print ("Welcome to your Entertainment Budget. What would you like to do??\n")
    ent_ops = int(input('Please input:\n1. Deposit 2. Withdrawal 3. Transfer \n4. Balance 5. Check funds 6. Home\n'))

    if ent_ops == 1:
        input_deposit = int(input('Enter your Entertainment budget:\n'))
        ent.deposit(input_deposit)
        print(f'You just deposited {input_deposit} in your entertainment wallet. Your new balance is {ent.get_balance()}\n')
        ent_operations()
    elif ent_ops == 2:
        input_withdrawal = float(input('How much would you like to withdraw:\n'))
        input_desc = input("What are you withdrawing for:\n")
        if input_withdrawal > ent.get_balance():
            print (f'insufficient funds for {input_desc}')
        elif input_withdrawal <= ent.get_balance():
            print(ent.withdraw(input_withdrawal, input_desc),'\n',f'Your balance after {input_desc} is:', ent.get_balance(),'\n')
        ent_operations()
    elif ent_ops == 3:
        input_transfer = float(input('How much would you like to transfer:\n'))
        input_category = int(input("Which category do you want to transfer to: 1. Food 2. Clothing\n"))
        if input_category == 1:
            if input_transfer > ent.get_balance():
                print("Insufficient funds for transfer ")
            elif input_transfer <= ent.get_balance():
                ent.transfer(input_transfer,food)
                print(f"Transfer of {input_transfer} was made from Entertainment to Food")
            else:
                print("Invalid input, please select from the available options")
                ent_operations()
            ent_operations()

        elif input_category == 2:
            if input_transfer > ent.get_balance():
                print ("Insufficient funds for transfer ")
            elif input_transfer <= ent.get_balance():
                ent.transfer(input_transfer,clothing)
                print(f"Transfer of {input_transfer} was made from Entertainment to Clothing")
            else:
                print("Invalid input, please select from the available options")
                ent_operations()
            ent_operations()
    elif ent_ops == 4:
        print(" Your Entertainment balance is:",food.get_balance())
        ent_operations()
    elif ent_ops == 5:
        input_check_funds = float(input('How much would you like to check:\n'))
        print(food.check_funds(input_check_funds))
        ent_operations()
    elif ent_ops == 6:
        budget_operations()
    else:
        print("Invalid input, please select from the available options")
        ent_operations()

  
def clothing_operations():

    print ("Welcome to your Clothing Budget. What would you like to do??\n")
    clothing_ops = int(input('Please input:\n1. Deposit 2. Withdrawal 3. Transfer \n4. Balance 5. Check funds 6. Home\n'))

    if clothing_ops == 1:
        input_deposit = int(input('Enter your Clothing budget:\n'))
        clothing.deposit(input_deposit)
        print(f'You just deposited {input_deposit} in your clothing wallet. Your new balance is {clothing.get_balance()}\n')
        clothing_operations()
    elif clothing_ops == 2:
        input_withdrawal = float(input('How much would you like to withdraw:\n'))
        input_desc = input("What are you withdrawing for:\n")
        if input_withdrawal > clothing.get_balance():
            print (f'insufficient funds for {input_desc}')
        elif input_withdrawal <= clothing.get_balance():
            print(clothing.withdraw(input_withdrawal, input_desc),'\n',f'Your balance after {input_desc} is:', clothing.get_balance(),'\n')
        clothing_operations()
    elif clothing_ops == 3:
        input_transfer = float(input('How much would you like to transfer:\n'))
        input_category = int(input("Which category do you want to transfer to: 1. Food 2. Entertainment\n"))
        if input_category == 1:
            if input_transfer > clothing.get_balance():
                print("Insufficient funds for transfer ")
            elif input_transfer <= clothing.get_balance():
                clothing.transfer(input_transfer,food)
                print(f"Transfer of {input_transfer} was made from Clothing to Food")
            else:
                print("Invalid input, please select from the available options")
                clothing_operations()
            clothing_operations()
       
        elif input_category == 2:
            if input_transfer > clothing.get_balance():
                return "Insufficient funds for transfer "
            elif input_transfer >= clothing.get_balance():
                clothing.transfer(input_transfer,ent)
                print(f"Transfer of {input_transfer} was made from Clothing to Entertainment")
            else:
                print("Invalid input, please select from the available options")
                clothing_operations()
        clothing_operations()
        
    elif clothing_ops == 4:
        print(" Your clothing balance is:",clothing.get_balance())
        clothing_operations()
    elif clothing_ops == 5:
        input_check_funds = float(input('How much would you like to check:\n'))
        print(clothing.check_funds(input_check_funds))
        clothing_operations()
    elif clothing_ops == 6:
        budget_operations()
    else:
        print("Invalid input, please select from the available options")
        clothing_operations()

budget_operations()


### commit change
### commit change dont wanna show
### Irrelevant to the above, just random comment below###

# budget = Category('Foodie')
# print(budget.name)

# print(type(ent))
