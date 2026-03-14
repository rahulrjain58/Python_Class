# l=[1,2,3,4,5,6,7,8,9,10]
# l1=filter(lambda x:x%2==0,l)
# print(list(l1))

# l2=lambda a,b: str(a)+" is bigger than "+ str(b) if a>b else str(b)+" is bigger than "+str(a)
# print(l2(6,5))


# l3 = (filter(lambda x: x % (x**(1/3)) == 0, l))
# print(list(l3))

# l1=[1,2,3,4]
# def square(n):
#     return n**2
# l2=list(map(square,l1))
# print(l2)

# l1=[1,2,3,4,5]
# squared_number=map(lambda x:x**2,l1)
# print(list(squared_number))

# l1=[23,34,54,67,34]
# def CheckEven(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"
# l2=list(map(CheckEven,l1))
# print(l2)  

# l1=[1,2,3,4,5]
# l2=[7,8,9,10,11]
# sum_number=map(lambda x,y:x+y,l1,l2)
# print(list(sum_number))

# word=["hello","world"]
# upper_word=map(lambda x:x.upper(),word)
# print(list(upper_word))

# l1=[1,2,3,4,5]
# l2=[7,8,9,10,11]
# Mul_number=map(lambda x,y:x*y,l1,l2)
# print(list(Mul_number))

# l1=["Rahul","harshil","om"]

# vowel_name=filter(lambda x: x[0] in "aeiou",l1)
# print(list(vowel_name))

# l1=["Rahul","harshil","om"]

# long_words=filter(lambda x: len(x)>4,l1)
# print(list(long_words))

# l1=["Rahul","","harshil","","om"]

# non_empty_string=filter(lambda x: x!="",l1)
# print(list(non_empty_string))

from functools import reduce
def add(x,y):
    return(x+y)
num=[1,2,3,4,5]
result=reduce(add,num)
print(result)
result=reduce(add,num,100)
print(result)