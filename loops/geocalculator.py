# -------------------- Geo Calculator --------------------

# Run Menu Continuously
while True:

    # Display Menu
    print("\nEnter Your Choice")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Exit")

    # Take Choice from User
    choice = int(input("Enter Your Choice: "))

    # Triangle Area
    if choice == 1:
        base = float(input("Enter Base: "))
        height = float(input("Enter Height: "))

        area = 0.5 * base * height

        print("Area of Triangle:", area)

    # Rectangle Area
    elif choice == 2:
        length = float(input("Enter Length: "))
        width = float(input("Enter Width: "))

        area = length * width

        print("Area of Rectangle:", area)

    # Circle Area
    elif choice == 3:
        radius = float(input("Enter Radius: "))

        area = 3.14 * radius ** 2

        print("Area of Circle:", area)

    # Exit Program
    elif choice == 4:
        print("Exiting the Program...")
        break

    # Invalid Choice
    else:
        print("Invalid Choice")
