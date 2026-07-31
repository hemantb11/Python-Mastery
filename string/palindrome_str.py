# String Slicing
s="india"
print(s[3:5])
print(s[3:])
print(s[0:3])
print(s[:3])
print(s[1:4])
print(s[0:5:2])


# String Slicing Example
s="india is my country!"
print(s[6:9])
print(s[12:17])
print(s[7:10])
print(s[16:20])
print(s[::-1])


# Palindrome String
ip=input("enter a string: ")
if ip==ip[::-1]:
    print("palindrome string")
else:
    print("not palindrome string")


# Count Alphabets and Digits
x="abc1234"
ct_digit=0
ct_count=0
for ch in x:
    if(ch>='0' and ch<='9'):
        ct_digit+=1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        ct_count += 1

print("alphabets:",ct_count)
print("digits:",ct_digit)


# Count Alphabets and Digits using String Functions
x="abc1234"
ct_digit=0
ct_count=0
for i in x:
    if(i.isdigit()):
        ct_digit+=1
    elif(i.isalpha()):
        ct_count+=1

print("alphabets:",ct_count)
print("digits:",ct_digit)


# Swap Case without String Function
x="sWapCaSe"
new_str=""
for i in x:
    if i>='a' and i<='z':
        new_str+=chr(ord(i)-32)
    elif i>='A' and i<='Z':
        new_str+=chr(ord(i)+32)
print(new_str)


# Print Characters with Odd ASCII Value
s="programming"
for i in s:
    if ord(i)%2!=0:
        print(i,ord(i))


# Remove Space from String
x=" hi"
new=""
for ch in x:
    if ch!=' ':
        new+=ch
print(new,len(new))


# Remove Space using not in
x=" hi"
print(len(x))
new=" "
for ch in x:
    if ' ' not in ch:
        new+=ch
print("ans",new,len(new))


# Print Unique Characters
a="programming"
unique=" "
for ch in a:
    if ch not in unique:
        unique+=ch
        print(unique)


# Count Words in String
x="i like python programming"
ct=1
for ch in x:
    if ch==" ":
        ct+=1
print(ct)