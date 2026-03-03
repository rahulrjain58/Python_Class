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


print("upper Characters: ",upper_char)
print("lower Characters: ",lower_char)
print("number Characters: ",num_char)
print("space Characters: ",space_char)
        