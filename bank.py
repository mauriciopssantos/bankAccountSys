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

    def reset_pin(self):
        choice=input(int("Press 1 if you forgot your pin or 2 to redefine it"))
        if choice==1:
            email=input("Write the email to receive the new pin:")
            if email==self.mail:
                self.mail=np.ran



