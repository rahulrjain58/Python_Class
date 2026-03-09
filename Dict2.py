d={1:"Jigar",2:"naresh",3:"Mahesh",4:"kishor"}
key=int(input("Enter an existing key: "))
value=input("Enter a value: ")
if key in d:
    d[key]=value
else:
    print("key is not present")
print(d)