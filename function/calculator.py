# Calculator Functions
def add(a,b):
    return(a+b)      # Return addition of two numbers

def sub(a,b):
    return(a-b)      # Return subtraction of two numbers

def mul(a,b):
    return(a*b)      # Return multiplication of two numbers

def div(a,b):
    return(a/b)      # Return division of two numbers


# Calculator Program
print("--------------Calculator--------------")

n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

ch=int(input("Enter Your Choice: "))


# Match Case
match ch:

    case 1:
        print("Addition is:", add(n1,n2))      # Call add() function

    case 2:
        print("Subtraction is:", sub(n1,n2))   # Call sub() function

    case 3:
        print("Multiplication is:", mul(n1,n2)) # Call mul() function

    case 4:
        print("Division is:", div(n1,n2))      # Call div() function

    case _:
        print("Invalid Choice")                # Execute if no case matches