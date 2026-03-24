from abc import ABC,abstractmethod

# class RBI(ABC):
#     @abstractmethod
#     def roi(r):
#         pass
# class SBI(RBI):
#     def show(self):
#         print("I am SBI")
#     def roi(self,r):
#         print("Rate of interest is ",r)

# class HDFC(RBI):
#     def show(self):
#         print("I am HDFC")
#     def roi(self,r):
#         print("Rate of interest is ",r)

# s1=SBI()
# s1.show()
# s1.roi(6.5)

# s2=HDFC()
# s2.show()
# s2.roi(7)

class Car(ABC):
    @abstractmethod
    def feature(self,seat,speed,fueltype):
        pass
class maruti(Car):
    def show(self):
        print("maruti")
    def feature(self, seat, speed, fueltype):
        print(f"maruti car has {seat} seats, max speed {speed} and fuel type {fueltype}")
c1=maruti()
c1.show()
c1.feature("5","200","CNG")