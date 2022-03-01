# #---------Class-----------------
# class Pet: 
#     def __init__(self,name,fullness,happiness): 
#         self.name = name
#         self.fullness=fullness
#         self.happiness=happiness

# #-------Methods----------- 
#     def eat_food(self): 
#         self.fullness 
#-------------main------------ 











#----------class----------------
from unicodedata import name


class BankAccount: 
    def __init__(self,name): 
        self.balance = 5000 #user starts with 5000
        self.name = str(name) #users name on account
        
        print("Hello" ,self.name, "your beginning balance is:" ,self.balance)

#-------Methods----------- 
    def name(self): 
        print("The name of your account:" + self.name)

    def deposit(self):            #user makes a deposit
        amount = int(input("Amount you want deposit:"))
        self.balance += amount 
        print("The amount that has been deposited", self.balance) 

    def withdraw(self):          # user makes a withdraw
        amount = int(input("Amount you want to withdrawl:"))
        if self.balance >= amount:
            self.balance -= amount 
            print(self.balance) 
        else: 
            print("Your balance is insufficent", self.balance)
    def display(self):             # displays user balance 
        print("Your balance is:", self.balance) 
# ---------------calling the methods--------------
person1 = BankAccount("Kenasia") 
person1.deposit()
person1.withdraw()
person1.display()
# print(person1)  
        
