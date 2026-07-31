# Import Parent Payment Class
from payment import payment      

class card(payment):

    # Override Parent pay() Method
    def pay(self):
        print("Card Payment Successful")
