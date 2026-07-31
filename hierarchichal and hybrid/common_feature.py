# Import Developer Class
from developer import developer

# Import Tester Class
from tester import tester


# Common Function (Polymorphism)
def cm(obj):
    # Calls calculate_bonus() method of the passed object
    obj.calculate_bonus()