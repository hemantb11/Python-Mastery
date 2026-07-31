# Import Required Classes
from payment_gateway import payment_gateway
from upi import upi
from card import card

# Create Payment Gateway Object
pg = payment_gateway()

# Create UPI Payment Object
u = upi()

# Create Card Payment Object
c = card()

# Display Payment Menu
ip = int(input("""
Payment Menu
1. UPI
2. Card
3. Exit

Enter Your Choice : """))

# Check User Choice
if ip == 1:

    # Process UPI Payment
    pg.payment_process(u)

elif ip == 2:

    # Process Card Payment
    pg.payment_process(c)

else:

    # Exit the Program
    print("Exit")