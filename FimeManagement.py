# file=open("hello.txt","w")
# file.write("This is file management demo using python.")
# file.close()
# print("File Written Successfully")

# print("*"*50)

# file=open("hello.txt","r")
# print(file.read())
# file.close()
# print("*"*50)

# file=open("hello1.txt","a")
# file.write("\n now this file is appended.")
# file.close()
# print("File Appended Successfully")

# print("*"*50)

# file=open("hello1.txt","r")
# print(file.read())
# file.close()
# print("*"*50)

# file=open("hello2.txt","w+")
# file.write("this is w+ operation.")
# print("Current file position: ", file.tell())
# file.seek(0)
# print("File data:",file.read())
# file.close()

# print("*"*50)

import json
user_data={}
user_data["name"]=input("enter your name: ")
user_data["age"]=int(input("enter your age: "))
user_data["city"]=input("enter your city: ")

with open("user_data.json","w") as file:
    json.dump(user_data,file,indent=4)

print("data added")