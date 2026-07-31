# Import the Parent Class
from payment import payment     

class upi(payment):

    # Child Class for UPI Payment
    # This method overrides the pay() method of the parent class
    def pay(self):
        print("UPI Payment Successful")