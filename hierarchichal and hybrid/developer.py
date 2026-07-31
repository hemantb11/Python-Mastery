# Import Parent Class
from person import person


# Developer Class (Inheritance)
class developer(person):

    # Constructor
    def __init__(self, name, id, skills, age):

        # Call Parent Class Constructor
        super().__init__(name, id, skills)

        # Initialize Developer's Own Variable
        self.age = age

    # Calculate Developer Bonus
    def calculate_bonus(self):

        # Take Salary from User
        salary = int(input("Enter Your Salary: "))

        # Calculate 15% Bonus
        bonus_amount = salary * 0.15

        # Call Parent Class Bonus Method
        super().bonus()

        # Display Bonus Amount
        print("Bonus Amount :", bonus_amount)

        # Display Total Salary
        print(f"Your Salary This Month Will Be {salary + bonus_amount}")

    # Developer Specific Method
    def development(self):
        print("I'm Writing Code")