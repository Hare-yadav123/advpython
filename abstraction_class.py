''' Abstraction is process of  hiding the implementation details from user side ,
only  the hilited set of services provied to the user.
like mobile Red button , call recived button ,all button .
'''
# inside abstract class we can define normal method
# we can't create object of the parent class 
# we used @abstacr method
'''from abc import ABC ,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass      # we can't create body of the abstract  class
    
    def show(self):      # concrete method
        print(" concrete method")
        
class child(Father):
    def disp(self):
        print("this is a child class")
        print("Defining abtract Method")       
c = child()
c.disp()
c.show()'''

# from abc import ABC,abstractmethod
# class Principle(ABC):
#     @abstractmethod
#     def subjct(self):
#         pass
#     def subp(self):
#         print("You have to  handle all things")
        
# class Teacher(Principle):
#     def subjct(self):
#         print("you have to tech hindi")
        
# class Scit(Principle):
#     def subjct(self):
#         print("you have to teach science")
# #p=Principle() #can't initiate class principle withw abstract method       
# t=Teacher()
# s=Scit()
# t.subjct()
# t.subp()
# print()
# s.subp()
# s.subjct()
# print(id(t))
# print(id(s))


#Example
# import first
# first.add      


from abc import ABC ,abstractmethod
class mom(ABC):
    @abstractmethod
    def abstractFun(self):
        print('hi')
        pass
    def concreat(self):
        print('this is conccreate method')
class douter:
    def abstractFun(self):
        print('this child class')
# m=mom()
# print(m.abstractFun())
d=douter()
print(d.abstractFun())











