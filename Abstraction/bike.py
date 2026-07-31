# Import Abstract Vehicle Class
from vehicle import vehicle

# Create Child Class
class bike(vehicle):

    # Override Abstract start() Method
    def start(self):
        print("Bike Starting......")


# Create Bike Object
obj = bike()

# Call start() Method
obj.start()