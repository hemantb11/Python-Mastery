from parent import A

class C(A):
    def __init__(self):
        print("def con C")
        super().__init__()


c1=C() 