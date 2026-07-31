# Create New File
file = open("myfile.txt", "x")
print(f"{file} created")


# Create File Using Exception Handling
try:
    file = open("batch45/demo.txt", "x")
    print(f"{file} created")

# Handle File Already Exists Error
except FileExistsError as e:
    print(e)


# Open File in Write Mode
with open("batch45/demo.txt", "w") as f:

    # Write Data into File
    f.write("how r you?")
    print("Data Inserted")


# Open File in Append Mode
with open("batch45/demo.txt", "a") as f:

    # Append New Data into File
    f.write("\nNew Data Added")
    print("Data Updated")