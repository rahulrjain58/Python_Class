class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        if isinstance(name,str) and len(name)>0:
            self.__name=name
        else:
            print("Invalid name. name should be non empty string")
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if isinstance(age,int) and age >= 0:
            self.__age=age
        else:
            print("Invalid age. age must be non negative digit.")


per=Person("Ram",30)
print(per.get_name())
print(per.get_age())
per.set_name("Rahul")
per.set_age(21)
print(per.get_name())
print(per.get_age())
per.set_name("")
per.set_age(-5)