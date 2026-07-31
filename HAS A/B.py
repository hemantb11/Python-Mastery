from A import engine
class car:
    def __init__(self,uip):
        self.age=90
        # object inject
        self.a=engine(uip)

    def car_details(self):
        print(self.a.show_engine())
        return f"car details are: {self.age}"

obj=car(200)
print(obj.age,obj.a.name,obj.a.horsepower,obj.a.brand)
print(engine)

print(obj.car_details())
