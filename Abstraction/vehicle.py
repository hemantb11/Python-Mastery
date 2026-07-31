# Import Required Modules
from abc import ABC, abstractmethod

# Create Abstract Parent Class
class vehicle(ABC):

    # Create Abstract Method
    @abstractmethod
    def start(self):
        pass