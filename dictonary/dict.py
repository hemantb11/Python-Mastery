stud={
    "rollno":101,
    "name":"ram",
    "age":30,
    "sub":["math","eng","java"],
    "marks":["80","90","56"]
}
print(stud)
print(stud.keys())
print(stud.values())
print(stud.items())


for key in stud:
    print(key)

for values in stud.values():
    print(values)

for k,v in stud.items():
    print(k,v)


for key in stud:
    if key=="sub":
        for v in stud[key]:
            print(v)


for i in range(len(stud["sub"])):
    print(f"{stud['sub'][i]} : {stud['marks'][i]}")



stud={
    101:{
        "name":"ram",
        "age":30,
        "sub":["math","eng","java"],
        "marks":(90,89,67)
    },
    102:{
        "name":"sita",
        "age":23,
        "sub":["math","eng","java"],
        "marks":(90,89,67) 
    },
    103:{
        "name":"sham",
        "age":24,
        "sub":["math","eng","java"],
        "marks":(90,89,67) 
    },
}

print
