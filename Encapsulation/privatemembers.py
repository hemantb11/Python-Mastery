class xyz:

    # Private Class Variable
    __a = 90

    # Public Class Variable
    x = 80

    # Getter Method (Access Private Variable)
    def getA(self):
        return self.__a

    # Public Method
    def abc(self):
        print("Public Method")

    # Private Method
    def __show(self):
        return "Private Method"

    # Public Method to Access Private Method
    def call_show(self):
        return self.__show()

    # Setter Method (Update Private Variable)
    def setvalue(self, newvalue):
        print("Existing Value :", self.__a)

        # Update Private Variable
        self.__a = newvalue

        print("Value Updated Successfully")
        print("New Value :", self.__a)


# Access Public Class Variable
print(xyz.x)

# Create Object
obj = xyz()

# Access Private Variable using Getter Method
print(obj.getA())

# Call Public Method
obj.abc()

# Access Private Method through Public Method
print(obj.call_show())

# Update Private Variable using Setter Method
obj.setvalue(100)

# Verify Updated Value
print(obj.getA())