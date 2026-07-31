# Parent Class
class person:

    # Constructor
    def __init__(self, name, id, skills):

        # Initialize Instance Variables
        self.name = name
        self.id = id
        self.skills = skills

    # Common Bonus Method
    def bonus(self):
        print("Year Bonus is.....")