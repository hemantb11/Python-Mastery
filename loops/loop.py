# For Loop with List
fruits = ["apple", "banana", "cherry"]
for fname in fruits:
    print(fname, end=" ")
print()

# For Loop with Numbers
no = [1, 2, 3, 4]
for i in no:
    print(i)

# For Loop with String
print()
s = "india"
for ch in s:
    print(ch, end=" ")

# Print Numbers from 1 to 5
print()
for i in range(1, 6):
    print(i, end=" ")

# Reverse Numbers from 10 to 1
print()
for i in range(10, 0, -1):
    print(i, end=" ")

# Print Numbers Divisible by 5 and 7
int(input("Enter a Number: "))
for i in range(1, 36):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")

# Break Statement
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")

# Continue Statement
for i in range(1, 6):
    if i == 4:
        continue
    print(i, end=" ")

# Sum of Numbers from 23 to 58
total = 0
for i in range(23, 59):
    total += i
print("The sum of numbers from 23 to 58 is:", total)

# Multiplication Table
num = int(input("Enter a Number: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

# Print Even Numbers
for i in range(500, 102, -1):
    if i % 2 == 0:
        print(i, end=" ")

# Factors of Number
num = 5
print("Factors of", num, "are:", end=" ")
for i in range(1, 6):
    if num % i == 0:
        print(i, end=" ")

# Factorial
num = 7
factorial = 1
for i in range(1, 8):
    factorial *= i
print("Factorial of", num, "is", factorial)

# Perfect Number
num = 6
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")

# Strong Number Logic (Extract Digits)
num = 145
while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10
