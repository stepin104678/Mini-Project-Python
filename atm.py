import os
import re  #import Regular expression library

from random import randint

class Account():

        def createAccount(self, name, initialDeposit, email_ID):
            self.secretPin = randint(1000, 9999)
            self.savingsAccounts[self.secretPin] = [name, initialDeposit, email_ID]
            print("Account has been created successfully.Your secret pin is ",self.secretPin)
    
class SavingsAccount(Account):  #creating Saving Account from Account
    def __init__(self):
        # [key][0] name ; [key][1] balance
        self.savingsAccounts = {} #creating dictionary to store the user name and amount
        
    def authenticate(self, name, secretPin):
        if secretPin in self.savingsAccounts.keys():
            if self.savingsAccounts[secretPin][0] == name:
                print("Authentication Successful")
                self.secretPin = secretPin
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawalAmount):     #calculate withdraw function and return acc balance
        print()
        if withdrawalAmount > self.savingsAccounts[self.secretPin][1]:
            print("Insufficient balance to withdraw.")
        else:
            self.savingsAccounts[self.secretPin][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            self.displayAccBalance()

    def deposit(self, depositAmount):
        print()
        self.savingsAccounts[self.secretPin][1] += depositAmount
        print("Deposit was successful.")
        output=open("op.txt","a+")
        output.write("Deposit was successful.")
        self.displayAccBalance()
        print()

    def displayAccBalance(self):
        ans1=print("Avaialble balance: ",self.savingsAccounts[self.secretPin][1])
        output=open("op.txt","w")               #writing account balance to the file
        ans=str("Avaialble balance: " + str(self.savingsAccounts[self.secretPin][1])+"\n")
        output.write(ans)
        output.close()
        #self.send_sms(self.savingsAccounts[self.secretPin][1])
    def email_Id_verification(self,email_ID):
        pattern = '[a-z 0-9]+@[a-z]+\.[a-z]{3}'
        test_string = email_ID
        result = re.match(pattern, test_string)
        if result:
            print("email ID verification successful.")
            return True
        else:
            print("email ID verification unsuccessful.")
            return False
        

bank_name=open("test.txt","r")                  #getting bank name as input from file
Name=bank_name.read()
print("Welcome to {} Bank".format(Name))

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to  Create a new  Saving Account")
    print("Enter 2 to Access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice == 1:
        print("Enter your name: ")
        name = input()
        print("Enter you Email_ID")
        email_ID = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit, email_ID)
    elif userChoice == 2:
        print("Enter your name: ")
        name = input()
        print("Enter your secret Pin: ")
        secretPin = int(input()) 
        authenticationStatus = savingsAccount.authenticate(name, secretPin)
        if authenticationStatus is True:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avialable balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                if userChoice == 1:
                    print("Enter an withdrawal amount")
                    try:
                        withdrawalAmount = int(input())
                        savingsAccount.withdraw(withdrawalAmount)
                    except ValueError:
                        print("Invalid Input for withraw!Give input as Integer")
                elif userChoice == 2:
                    print("Enter an amount to be deposited")
                    try:
                        depositAmount = int(input())
                        savingsAccount.deposit(depositAmount)
                    except ValueError:
                        print("Invalid Input for deposit!Give input as Integer")
                elif userChoice == 3:
                    savingsAccount.displayAccBalance()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
        quit()
