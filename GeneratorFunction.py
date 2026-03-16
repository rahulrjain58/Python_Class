# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b

# fib1=fib(10)

# for num in fib1:
#     print(num)



# def count_up_to(n):
#     count=1
#     while count<=n:
#         yield count
#         count+=1

# counter=count_up_to(5)
# for num in counter:
#     print(num)

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
# gen=simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def simple_generator():
#     num=1
#     while num<=1000:
#         yield num
#         num=num+100
    
# gen=simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

num=[1,2,3,4]
iterator=iter(num)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))