s=input("Enter a String: ")
upper_char=0
lower_char=0
num_char=0
space_char=0
for i in s:
    if i.isupper():
        upper_char+=1
    elif i.islower():
        lower_char+=1
    elif i.isnumeric():
        num_char+=1
    elif i.isspace():
        space_char+=1


print(upper_char)
print(lower_char)
print(num_char)
print(space_char)
        