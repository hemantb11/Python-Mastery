# Import Required Modules
from abc import ABC, abstractmethod

# Create Abstract Parent Class
class ATM(ABC):

    # Parameterized Constructor
    def __init__(self, bal):
        self.bal = bal

    # Getter Method to Return Balance
    def getbal(self):
        return self.bal

    # Abstract Method for Withdrawal
    @abstractmethod
    def withdraw(self, amount):
        pass
