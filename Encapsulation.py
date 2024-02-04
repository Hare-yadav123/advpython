# Encapsulation provide security hiding the data outside of the world
# encupsulation refers to  wrapping up(lapetna,sametna) of data under a single unit
# it is machinism that bind code and data that it manipulates

'''
python provides access to all the variable and method globly,
--by using encapsulation,we can protect the variable and method acess globlly,
by makeng  it private and protected.

note= single underscore _protected
double underscore __ private
'''
# class car:
#     handle="round"
#     bark="dogy"
#     def __init__(self,pet,milk):
#         self._pet=pet
#         self.__mammel=milk
#         self.__show()
#     def __show(self):
#         print(self._pet) 
#         print(self.__mammel)
#         print(self.__private_method())
#         print(self.__show())  
#     def __private_method(self):
#         print('how ra u')
# s=car("cow", "goat") 
# print(car.bark)
# print(car.handle)
# s.__show()
# s.__private_method()


# class A:
#     _s=20
#     __c=50
#     def disp(self):
#        print(self._s)
#        print(self.__c)
# a=A()
# a.disp()
# print('outside of the class ',A._s)
# # print('outside of the class ',A.__c)

class Encp:
    age_=50
    name__='ram'
    def _disp(self):
        print(self.age_)
        print(self.name__)
e=Encp()
e._disp()
print(f'outsid of class we can print :{e.age_}and :{e.name__}')