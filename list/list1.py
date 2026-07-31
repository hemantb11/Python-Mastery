x=[101,57,6,98,32,57,98]
print(x)
ip=int(input("Enter your key to find: "))
flag=0
for i in x:
    if ip==i:
        print("key found")
        flag=1
if flag==0:
        print("key not found")


# duplicate element find in list
x=[101,57,6,98,32,57,98]
print(x)
print("duplicate keys")
y=[]
for i in x:
    if x.count(i)>1 and i not in y:
        print(i)
        y.append(i)


# print unique element
x=[101,57,6,98,32,57,98]
print(x)
print("Unique element: ")
for i in x:
    if x.count(i)<=1:
        print(i)









