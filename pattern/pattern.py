# Hollow Pattern
for i in range(1,6):
    for j in range(1,6):
        if((i==1 or j==1 or i==5 or j==5) or (i==3 and j==3)):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()


# Star Pattern
n=4
for i in range(1,n+1):
    print("*"*i)


# Number Pattern
n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()


# Reverse Number Pattern
n=4
for i in range(4,0,-1):
    for j in range(i):
        print(i,end="")
    print()


# Alternate 1 and 0 Pattern
n=4
for i in range(1,n+1):
    for j in range(i):
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()


# Odd Number Pattern
n=4
for i in range(1,n+1):
    for j in range(i):
        print(2*i-1,end=" ")
    print()


# Zero-One Pattern
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print("0",end="")
        else:
            print("1",end="")
    print()
