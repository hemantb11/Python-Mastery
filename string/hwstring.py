# Reverse String without using String Function
s="hello"
ct=0
for i in s:
    ct+=1

rev=" "
for i in range(ct-1,-1,-1):
    rev+=s[i]

print(rev)


# Count Vowels, Even ASCII Characters and Odd ASCII Characters
s="maharashtra"

even_c=0
odd_c=0
vowel_count=0

vowels="aeiouAEIOU"

for i in s:
    if i in vowels:
        vowel_count += 1

for i in s:
    if ord(i)%2==0:
        even_c += 1
    else:
        odd_c += 1

print("Vowel count:", vowel_count)
print("Even char count:", even_c)
print("Odd char count:", odd_c)


# Convert String to Uppercase without using String Function
s="hello"

for i in s:
    print(chr(ord(i)-32),end=" ")


# Replace 'p' with 'x' without using String Function
s="python_programming"

for i in s:
    if i=='p':
        print("x",end=" ")
    else:
        print(i,end=" ")
