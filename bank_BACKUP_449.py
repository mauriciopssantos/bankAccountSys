import numpy as np
import smtplib, ssl

class bank_account:
    
    def __init__(self, name, pin):
        self.name=name
        self.pin=pin
        self.adress=""
        self.mail="mary@gmail.com"
        self.account_type=""
        self.balance=0
        self.check_number_monthly=20
<<<<<<< HEAD
        self.silver_type = " "
        self.gold_type = " "
=======
        self.password="hello"

>>>>>>> fae7c4060aa09e89d5f3205609dde0702ba8c42d
    def reset_pin(self):
        choice=input(int("Press 1 if you forgot your pin or 2 to redefine it"))
        if choice==1:
            email=input("Write the email to receive the new pin:")
            if email==self.mail:
                port = 465
                password = input("Type your password and press enter: ")
                self.pin=np.random.randn(6)
                # Create a secure SSL context
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login("my@gmail.com", password)
                # TODO: Send email here






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


