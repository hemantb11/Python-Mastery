# Factorial Function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


# Prime Number Function
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


# Reverse Number Function
def revno(n):
    return int(str(n)[::-1])


# Menu Driven Program
while True:
    print("Choose an option:")
    print("1. Factorial")
    print("2. Prime Number")
    print("3. Reverse Number")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        num=int(input("Enter a number to find its factorial: "))
        print("Factorial of",num,"is",factorial(num))

    elif choice==2:
        num=int(input("Enter a number to check if it's prime: "))
        print(num,"is prime:",prime(num))

    elif choice==3:
        num=int(input("Enter a number to reverse: "))
        print("Reversed number is",revno(num))

    elif choice==4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice.")
