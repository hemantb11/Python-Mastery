# Import Abstract ATM Class
from ATM import ATM

# Create Child Class
class SBIATM(ATM):

    # Override Abstract withdraw() Method
    def withdraw(self, amount):

        # Check Valid Withdrawal Amount
        if amount > 0:

            # Deduct Amount from Balance
            self.bal -= amount

            # Display Debit Message
            print(f"Amount ₹{amount} Debited Successfully")

        else:

            # Display Invalid Amount Message
            print("Invalid Amount")


# Create SBIATM Object
obj = SBIATM(1000)

# Display Current Balance
print("Available Balance :", obj.getbal())

# Withdraw Amount
obj.withdraw(300)

# Display Updated Balance
print("Remaining Balance :", obj.getbal())