# Import Developer Class
from developer import developer

# Import Tester Class
from tester import tester

# Import Common Function
from common_feature import cm


# Display Menu
choice = int(input("1. Developer\n2. Tester\n3. Exit\nEnter Your Choice: "))

# Initially No Object
obj = None

# Create Developer Object
if choice == 1:
    obj = developer("Ram", 101, "Python", 90)

# Create Tester Object
elif choice == 2:
    obj = tester("Sita", 102, "Java", 88)

# Invalid Choice
else:
    print("Invalid Choice")


# Check Object Created or Not
if obj:

    # Call Common Function (Polymorphism)
    cm(obj)

else:
    print("No Object Created")