from A import A
class B(A):
    def abc(self):
        print("this is class b method")

    def __init__(self):
        print("this is class b constructor")

obj=B()
print(B.mro())