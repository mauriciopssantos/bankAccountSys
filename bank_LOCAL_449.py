import numpy as np

class bank_account:
    
    def __init__(self, name, pin):
        self.name=name
        self.pin=pin
        self.adress=""
        self.mail="mary@gmail.com"
        self.account_type=""
        self.balance=0
        self.check_number_monthly=20
        self.silver_type = " "
        self.gold_type = " "
    def reset_pin(self):
        choice=input(int("Press 1 if you forgot your pin or 2 to redefine it"))
        if choice==1:
            email=input("Write the email to receive the new pin:")
            if email==self.mail:
                self.mail=np.ran






    def create_account(self):
        self.address = input("Hello {} enter your address to create your account: ").format(self.name)
        
        while self.account_type != 1 or self.account_type != 2:
            self.account_type= int(input("Choose your account type (enter one of the following numbers):\n1 - Silver Account : ...\n2 - Gold Account : ..."))
            if self.account_type == 1:
                self.account_type == self.silver_type
            elif self.account_type ==2:
                self.account_type == self.gold_type
            else:
                print("Please try again!")

        self.balance = int(input("Enter a balance to activate your account: "))


