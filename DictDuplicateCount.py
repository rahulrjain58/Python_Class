d={1:"1",2:"2",3:"1",4:"3",5:"2",6:"1",7:"3",8:"3",9:"1",}
k={}
for x in d.values():
    k[x] = k.get(x, 0) + 1

for x,y in k.items():
    if y>1:
        print(x, ":",y )