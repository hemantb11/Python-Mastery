# # Reverse String
s="python"
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print("Reverse String is:",rev)


# Palindrome String
s=input("Enter String: ")
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]

if s==rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Convert Lowercase to Uppercase
s="hello"
new_str=""
for ch in s:
    if ch>='a' and ch<='z':
        new_str+=chr(ord(ch)-32)
    else:
        new_str+=ch
print(new_str)


# Convert Uppercase to Lowercase
s="HELLO"
new_str=""
for ch in s:
    if ch>='A' and ch<='Z':
        new_str+=chr(ord(ch)+32)
    else:
        new_str+=ch
print(new_str)


# Swap Case
s="HeLlO pYtHoN"
new=""
for ch in s:
    if ch>='a' and ch<='z':
        new+=chr(ord(ch)-32)
    elif ch>='A' and ch<='Z':
        new+=chr(ord(ch)+32)
    else:
        new+=ch
print(new)


# Sort String Characters
s="hello"
print(s)

s=list(s)
print(s)

sorted_str=sorted(s)
print(sorted_str)

new_str="-".join(sorted_str)
print(new_str)