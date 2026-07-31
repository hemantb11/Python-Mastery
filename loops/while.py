# -------------------- Count Digits --------------------
num = 123456
ct = 0
while num > 0:
    ct += 1
    num //= 10
print(ct)


# -------------------- Sum of Digits --------------------
num = 1234
sum = 0
while num > 0:
    rem = num % 10
    sum += rem
    num //= 10
print(sum)


# -------------------- Reverse Number --------------------
num = 1234
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
print(rev)


# -------------------- Palindrome Number --------------------
num = int(input("Enter a Number: "))
temp = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# -------------------- Armstrong Number --------------------
num = int(input("Enter a Number: "))
temp = num
sum = 0

while temp > 0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10

if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


# -------------------- Happy Number --------------------
num = 24

while num != 1 and num != 4:
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem * rem
        num //= 10
    num = sum

if num == 1:
    print("Happy Number")
else:
    print("Not Happy Number")


# -------------------- Buzz Number --------------------
num = int(input("Enter a Number: "))

if num % 7 == 0 or num % 10 == 7:
    print("Buzz Number")
else:
    print("Not Buzz Number")


# -------------------- Square Star Pattern --------------------
n = int(input("Enter Number: "))

i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# -------------------- Print Numbers 1 to 9 (3x3) --------------------
num = 1

for i in range(1, 4):
    for j in range(1, 4):
        print(num, end=" ")
        num += 1
    print()


# -------------------- Diagonal Pattern --------------------
num = 1

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print(num, end=" ")
        else:
            print("0", end=" ")
    print()


# -------------------- Hollow Square Pattern --------------------
n = 4

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()


# -------------------- Happy Numbers (1 to 100) --------------------
for num in range(1, 101):
    temp = num

    while temp != 1 and temp != 4:
        sum = 0
        while temp > 0:
            rem = temp % 10
            sum += rem * rem
            temp //= 10
        temp = sum

    if temp == 1:
        print(num, end=" ")


# -------------------- Happy Numbers (201 to 5000) --------------------
for i in range(201, 5001):
    temp = i

    while temp != 1 and temp != 4:
        sum = 0
        while temp > 0:
            rem = temp % 10
            sum += rem * rem
            temp //= 10
        temp = sum

    if temp == 1:
        print(i, end=" ")


# -------------------- Neon Number --------------------
num = int(input("Enter a Number: "))

sq = num ** 2
sum = 0

while sq > 0:
    rem = sq % 10
    sum += rem
    sq //= 10

if num == sum:
    print("Neon Number")
else:
    print("Not Neon Number")


# -------------------- Prime Numbers (1 to 100) --------------------
for i in range(1, 101):
    ct = 0

    for j in range(1, i + 1):
        if i % j == 0:
            ct += 1

    if ct == 2:
        print(i, end=" ")


# -------------------- Spy Number --------------------
num = int(input("Enter a Number: "))

temp = num
sum = 0
mul = 1

while temp > 0:
    rem = temp % 10
    sum += rem
    mul *= rem
    temp //= 10

if sum == mul:
    print("Spy Number")
else:
    print("Not Spy Number")


# -------------------- Harshad Number --------------------
num = int(input("Enter a Number: "))

temp = num
sum = 0

while temp > 0:
    rem = temp % 10
    sum += rem
    temp //= 10

if num % sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
