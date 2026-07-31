class vehicle:
    # Constructor
    def __init__(self, fuel_type, brand):
        # Instance variable to store fuel type
        self.fuel_type = fuel_type

        # Instance variable to store brand name
        self.brand = brand

    # Method to start the vehicle
    def start(self):
        return "vehicle is starting"

    # Method to stop the vehicle
    def stop(self):
        return "vehicle is stopping"