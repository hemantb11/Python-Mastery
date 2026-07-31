class engine:
    brand="xyz"
    def  __init__(self,horsepower):
        # instant variable manually declared
        self.name = "V8"
        # user input when obj created at that time user will send some input
        self.horsepower=horsepower

    def show_engine(self):
        return f"engine details are: {self.brand}\n {self.horsepower}\n{self.name}"
