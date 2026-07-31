# Parent Class
class person:

    # Constructor
    def __init__(self, name, city, age):

        # Instance Variables
        self.name = name
        self.city = city
        self.age = age

    # Instance Method
    def display_personal_details(self):

        print("======= Personal Info =======")

        # Display Personal Details
        print(f"Name: {self.name}  Age: {self.age}  City: {self.city}")