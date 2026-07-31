# ZeroDivisionError Example

print("Start")

try:
    # Divide Number by Zero
    print(10 / 0)

# Handle ZeroDivisionError
except ZeroDivisionError:
    print("Don't Divide by Zero")
print("Program End")


# ValueError Example
print("Start")
try:
    # Accept Integer Input
    ip = int(input("Enter the Number : "))

    # Display User Input
    print(ip)

# Handle ValueError
except ValueError as e:
    print(e)
print("Program End")


# IndexError Example
print("Start")
try:
    # Create List
    x = [10, 20]
    # Access Invalid Index
    print(x[9])
# Handle IndexError
except IndexError:
    print("Please Enter Valid Index")
print("Program End")


# Multiple Except Blocks Example
print("Start")
try:
    # Create List
    x = [10, 20]
    # Access Invalid Index
    print(x[3])
    # Divide by Zero
    print(10 / 0)
# Handle IndexError
except IndexError as e:
    print(e)
# Handle ZeroDivisionError
except ZeroDivisionError:
    print("Don't Divide by Zero")
print("Program End")


# Multiple Exception Handling Example
print("Start")
try:
    # Accept Integer Input
    ip = int(input("Enter the Number : "))
    # Divide Number
    print(10 / ip)
# Handle Multiple Exceptions
except (ValueError, ZeroDivisionError):
    print("Something Went Wrong")
print("Program End")


# Finally Block Example
print("Start")
try:
    # Accept Integer Input
    ip = int(input("Enter the Number : "))
    # Divide Number
    print(10 / ip)
# Handle Multiple Exceptions
except (ValueError, ZeroDivisionError):
    print("Something Went Wrong")
# Finally Block Always Executes
finally:
    print("I am Always Execute")
print("Program End")




# Create User Defined Exception
class AgeError(Exception):
    pass

print("Start")
try:
    # Accept User Age
    age = int(input("Enter Your Age : "))
    # Check Eligibility
    if age > 18:
        print("Eligible")
    # Raise Custom Exception
    else:
        raise AgeError("Age Should be Greater Than 18")
# Handle User Defined Exception
except AgeError as e:
    print(e)
print("======")


