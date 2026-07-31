from parent import A

class B(A):
    def __init__(self):
        print("def con B")
        super().__init__()


c1=B()
