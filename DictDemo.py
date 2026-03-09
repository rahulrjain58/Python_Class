d={101:"Khushi",899:"Riddhi",767:"Anshu",545:"Shivani",323:"Zeel",122:"Chaitanya"}
print(d)
print(d[323])
print(d.get(101))
print(d.items())
print(d.keys())
print(d.pop(767))
d.popitem()
print(d)

d1={767:"Anshu",122:"Chaitanya"}
d.update(d1)
print(d)
print(d.values())

for i in d:
    print(i)

for i in d:
    print(i, ": ", d[i])