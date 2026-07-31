# Import vehicle class from vehicle.py
from vehicle import vehicle

# bike class inherits vehicle class
class bike(vehicle):

    # Constructor
    def __init__(self, fuel_type, brand, color, price):

        # Store bike color
        self.color = color

        # Store bike price
        self.price = price

        # Call parent (vehicle) constructor
        super().__init__(fuel_type, brand)

    # Bike specific method
    def ride(self):
        return "Bike rides so fast"

    # Method Overriding using super()
    def custom_start(self):

        # Call parent class start() method
        print(super().start())

        # Return bike-specific start sound
        return "BRUMHHHH"

    # Method to calculate fuel consumption and remaining distance
    def km_travel(self):

        # Take distance travelled from user
        km = float(input("Enter distance traveled (km): "))

        # Take bike mileage from user
        average = float(input("Enter bike mileage (km/L): "))

        # Take available fuel in tank
        fuel_available = float(input("Enter fuel available in tank (L): "))

        # Calculate fuel used
        fuel_used = km / average

        # Calculate remaining fuel
        remaining_fuel = fuel_available - fuel_used

        # Calculate how many more kilometers bike can travel
        remaining_distance = remaining_fuel * average

        # Display all results
        print(f"\nDistance Travelled : {km} km")
        print(f"Fuel Used          : {fuel_used:.2f} L")
        print(f"Fuel Remaining     : {remaining_fuel:.2f} L")
        print(f"Bike can travel    : {remaining_distance:.2f} km more")


# Create object of bike class
b1 = bike("Petrol", "BMW", "Black", 1000000)

# Call km_travel() method
b1.km_travel()