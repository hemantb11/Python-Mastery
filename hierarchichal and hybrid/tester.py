# Import Parent Class
from person import person


# Tester Class (Inheritance)
class tester(person):

    # Constructor
    def __init__(self, name, id, skills, age):

        # Call Parent Class Constructor
        super().__init__(name, id, skills)

        # Initialize Tester's Own Variable
        self.age = age

    # Calculate Tester Bonus
    def calculate_bonus(self):

        # Take Salary from User
        salary = int(input("Enter Your Salary: "))

        # Calculate 20% Bonus
        bonus_amount = salary * 0.20

        # Call Parent Class Bonus Method
        super().bonus()

        # Display Bonus Amount
        print("Bonus Amount :", bonus_amount)

        # Display Total Salary
        print(f"Your Salary This Month Will Be {salary + bonus_amount}")

    # Tester Specific Method
    def testing(self):
        print("I'm Testing Application")