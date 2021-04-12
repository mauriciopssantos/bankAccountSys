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
        self.password="hello"

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



