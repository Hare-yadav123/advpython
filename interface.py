
'''
interface is a nothing but abstract class which contain only abstact method but not any norlmal method
#we can't create object of the interface
#we use interface , when an action is common but implimentation is different
# all child class should be inherit interface class
'''
from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass           
class Child(Father):
    def disp1(self):
        print("this is a child class")
        print("Defining abtract Method") 
        print("************************") 
class Grandchild(Child):
    def disp2(self):
        print("this is a disp2 finction")
        print("Defining abtract Method" )
         
c = Grandchild()
c.disp1()
c.disp2()

class Shape(ABC):
    @abstractmethod
    def show(self):
        pass   
    
class squre(Shape):
    def show(self):
        print('There are four side of object....')
class circle(Shape):
    def show(self):
        print('circle has cilcle....')

s=squre()  
s.show()
c=circle() 
c.show()
