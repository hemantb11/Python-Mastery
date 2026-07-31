x=[10,20,30]
print(x)
print(x[1])
print(x[2])
x[2]=300
print(x[2])


for items in x:
    print(items)


# add element by user input
x=[]
print(x)
for i in range(5):
    ip=input(f"enter {i+1} element ")
    x.append(ip)
print(x)


x=[1,2]
print(x)
x.extend([3,4])
print(x)


x=[11,13]
x.insert(1,12)
print(x)

x=[10,8,9,"hii",90,89]
x.remove("hii")   #remove use for element
x.pop(4)          #pop use for index no remove
print(x)

x.clear()         #clear hole list
print(x)



x=[10,20,40,60,10,30]
print(x.count(10))
print(x.index(30))

x.sort()
print(x)

x.reverse()
print(x)

y=x.copy()
print(y)


# function
x=[78,90,12,8]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x,reverse=True))


x=[10,20,45,30]

count=0
for i in x:
    count+=1
print(count)


max=0
for i in x:
    if i >= max:
        max=i
print(max)


stud=[1,"ram",2,"sita",3,"pooja"]
print(stud)
for i in range(len(stud)):
    if i%2==0:
        print(stud[i])


stud=[1,"ram",45,2,"sita",78,3,"pooja",90] 
for i in range(0,len(stud),3):
    print("ID: ",stud[i])
    print("name: ",stud[i+1])
    print("marks: ",stud[i+2])
    print()


